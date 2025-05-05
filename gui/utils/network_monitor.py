import threading
import time
from .network_utils import check_internet_http, check_internet_ping


class NetworkMonitor:
    def __init__(self, on_status_change, interval=5):
        """
        :param on_status_change: функция-колбек, которая принимает bool (online/offline)
        :param interval: время между проверками в секундах
        """
        self.on_status_change = on_status_change
        self.interval = interval
        self._online_status = None
        self._running = False

    def start(self):
        if not self._running:
            self._running = True
            monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
            monitor_thread.start()

    def stop(self):
        self._running = False

    def _monitor_loop(self): 
        while self._running:
            try:
                online = check_internet_http()
                if not online:
                    online = check_internet_ping()

                if online != self._online_status:
                    self._online_status = online
                    self.on_status_change(online)
            except Exception as e:
                print(f"Error checking internet connection: {e}")
            time.sleep(self.interval)