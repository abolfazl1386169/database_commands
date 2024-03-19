import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sqlite3
import bcrypt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('صفحه ورود')
        layout = QVBoxLayout()
        
        self.username_label = QLabel('نام کاربری:')
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('حداقل 4 کاراکتر')
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        
        self.password_label = QLabel('کلمه عبور:')
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('حداقل 6 کاراکتر')
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        
        self.login_button = QPushButton('ورود')
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)
        
        self.setLayout(layout)
    
    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        if len(username) < 4 or len(password) < 6:
            QMessageBox.critical(self, 'خطا', 'نام کاربری باید حداقل 4 کاراکتر و کلمه عبور باید حداقل 6 کاراکتر باشد.')
            return
        
        conn = sqlite3.connect('students_database.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        
        hashed_password = result[0].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            print("secsesful!!")
        else:
            print("not secsesful!!")
        conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())