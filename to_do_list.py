import mysql.connector
from datetime import datetime

# Connect to MySQL
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="todo_db"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create tasks table
def create_table():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                task VARCHAR(255) NOT NULL,
                due_date DATETIME NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        connection.commit()
        cursor.close()
        connection.close()

# Add a new task
def add_task(task, due_date):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO tasks (task, due_date) VALUES (%s, %s)"
        cursor.execute(query, (task, due_date))
        connection.commit()
        print("Task added successfully!")
        cursor.close()
        connection.close()

# View all tasks
def view_tasks():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        query = "SELECT id, task, due_date, created_at FROM tasks"
        cursor.execute(query)
        results = cursor.fetchall()
        print("\nTo-Do List:")
        for row in results:
            print(f"ID: {row[0]}, Task: {row[1]}, Due Date: {row[2]}, Created At: {row[3]}")
        cursor.close()
        connection.close()

# Main program
def main():
    create_table()
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter the task: ")
            due_date_str = input("Enter due date (YYYY-MM-DD HH:MM:SS): ")
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M:%S")
                add_task(task, due_date)
            except ValueError:
                print("Invalid date format. Please try again.")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()