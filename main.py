import sys
from PyQt6.QtWidgets import QApplication
from backend import Login, CreateAccount

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = Login()
    createUser_window = CreateAccount()
    sys.exit(app.exec())
