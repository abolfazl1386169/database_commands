from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
import sys
import sqlite3

# Create the application
app = QApplication(sys.argv)

# Create the main window
main_window = QWidget()
main_window.setWindowTitle('User Display')
main_window.setGeometry(100, 100, 325, 300)

# Create a layout
main_layout = QVBoxLayout()

# Create a table to display the data
table = QTableWidget()
table.setColumnCount(3)
table.setHorizontalHeaderLabels(['Name', 'Phone Number', 'Score'])

# Connect to the database
conn = sqlite3.connect('students_database.db')
cursor = conn.cursor()

# Read data from the database
cursor.execute('SELECT * FROM ALI')
data = cursor.fetchall()

# Populate the table with data
for row_num, row_data in enumerate(data):
    table.insertRow(row_num)
    for col_num, col_data in enumerate(row_data):
        item = QTableWidgetItem(str(col_data))
        table.setItem(row_num, col_num, item)

# Close the connection
conn.close()

# Add the table to the layout
main_layout.addWidget(table)
main_window.setLayout(main_layout)

# Show the main window
main_window.show()

# Start the application event loop
sys.exit(app.exec())