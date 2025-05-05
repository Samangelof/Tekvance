import customtkinter as ctk
from gui.utils.network_monitor import NetworkMonitor


class StatusManager:
    """
    Управляет статусными индикаторами в приложении (сеть и др.).
    Отслеживает различные состояния и отображает их в интерфейсе.
    """
    def __init__(self, master):
        self.master = master
        
        # Индикатор сетевого подключения
        self.status_label = ctk.CTkLabel(master, text="🔴 Offline", text_color="red")
        self.status_label.grid(row=0, column=2, sticky="se", pady=5, padx=10)
        

        self.network_monitor = NetworkMonitor(self.on_network_change)
        self.network_monitor.start()
    
    def on_network_change(self, online):
        """
        Обработчик изменения статуса сети.
        
        :param online: Флаг, указывающий на наличие подключения
        """
        self.master.after(0, lambda: self.update_online_status(online))
    
    def update_online_status(self, online):
        """
        Обновляет индикатор сетевого статуса.
        
        :param online: Флаг, указывающий на наличие подключения
        """
        status_text = "🟢 Online" if online else "🔴 Offline"
        color = "green" if online else "red"
        self.status_label.configure(text=status_text, text_color=color)
    
    def cleanup(self):
        """Освобождает ресурсы при закрытии приложения"""
        if hasattr(self, 'network_monitor'):
            self.network_monitor.stop()