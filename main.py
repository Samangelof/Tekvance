from gui.app import TekVanceApp
from gui.config import load_app_config


if __name__ == "__main__":
    config = load_app_config()
    app = TekVanceApp(config)
    app.mainloop()