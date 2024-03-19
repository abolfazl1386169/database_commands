from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import sys
import sqlite3

class UserForm(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('User Information Form')
        self.setGeometry(100, 100, 300, 200)

        # Create layout
        layout = QVBoxLayout()

        # Add widgets to layout
        self.name_label = QLabel('Name:')
        layout.addWidget(self.name_label)

        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        self.family_label = QLabel('Family Name:')
        layout.addWidget(self.family_label)

        self.family_input = QLineEdit()
        layout.addWidget(self.family_input)

        self.national_id_label = QLabel('National ID:')
        layout.addWidget(self.national_id_label)

        self.national_id_input = QLineEdit()
        layout.addWidget(self.national_id_input)

        self.phone_label = QLabel('Phone:')
        layout.addWidget(self.phone_label)

        self.phone_input = QLineEdit()
        layout.addWidget(self.phone_input)

        self.db_path_label = QLabel('Database Path:')
        layout.addWidget(self.db_path_label)

        self.db_path_input = QLineEdit()
        layout.addWidget(self.db_path_input)

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submit_info)
        layout.addWidget(self.submit_button)

        # Set the layout on the application's window
        self.setLayout(layout)

    def submit_info(self):
        name = self.name_input.text()
        family = self.family_input.text()
        national_id = self.national_id_input.text()
        phone = self.phone_input.text()
        db_path = self.db_path_input.text()

        # Here, instead of printing, you would add your logic to save the data to the database
        print(f"Name: {name}, Family: {family}, National ID: {national_id}, Phone: {phone}, DB Path: {db_path}")
        self.save_to_database(name, family, national_id, phone, db_path)

    def save_to_database(self, name, family, national_id, phone, db_path):
        # Establish connection to the database
        # Note: You must handle any errors associated with file paths or database operations
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (name TEXT, family_name TEXT, national_id TEXT, phone TEXT)''')

        # Insert a row of data
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
                       (name, family, national_id, phone))
        
        # Save (commit) the changes
        conn.commit()

        # Close the connection
        conn.close()
        print("Information saved successfully.")

def main():
    app = QApplication(sys.argv)
    main_window = UserForm()
    main_window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()