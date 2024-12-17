# import mysql.connector

# connection=mysql.connector.Connect(
#     host="localhost",
#     user="gilbert",
#     password="gilbert0987",
#     database="mydb"
# )
# print("connected successfully")
# connection.close()



# CREATE TABLE todo_list (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     create_date TEXT,
#     subject TEXT,
#     work_date TEXT
# );
# import sqlite3
# from datetime import datetime

# # Function to establish a connection to the database
# def connect_db():
#     conn = sqlite3.connect('todo_list.db')
#     return conn

# # Function to create the table if it doesn't exist
# def create_table(conn):
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS todo_list (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             create_date TEXT,
#             subject TEXT,
#             work_date TEXT
#         )
#     ''')
#     conn.commit()

# # Function to add a task to the database
# def add_task(conn, subject, work_date):
#     create_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current timestamp
#     cursor = conn.cursor()
#     cursor.execute('''
#         INSERT INTO todo_list (create_date, subject, work_date)
#         VALUES (?, ?, ?)
#     ''', (create_date, subject, work_date))
#     conn.commit()
#     print(f"Task '{subject}' added successfully!")

# # Function to view all tasks in the database
# def view_tasks(conn):
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM todo_list')
#     tasks = cursor.fetchall()
#     if tasks:
#         print("\n--- To-Do List ---")
#         for task in tasks:
#             print(f"ID: {task[0]}, Created: {task[1]}, Subject: {task[2]}, Work Date: {task[3]}")
#     else:
#         print("No tasks found.")

# # Main function to drive the program
# def main():
#     conn = connect_db()  # Connect to the database
#     create_table(conn)    # Create the table if it doesn't exist

#     while True:
#         print("\nTo-Do List Application")
#         print("1. Add task")
#         print("2. View tasks")
#         print("3. Exit")
        
#         choice = input("Choose an option (1/2/3): ")

#         if choice == '1':
#             # User input for task subject and work date
#             subject = input("Enter task subject: ")
#             work_date = input("Enter work date (YYYY-MM-DD): ")
#             add_task(conn, subject, work_date)  # Add the task to the database
        
#         elif choice == '2':
#             # Display all tasks
#             view_tasks(conn)
        
#         elif choice == '3':
#             print("Exiting the application.")
#             break  # Exit the loop
        
#         else:
#             print("Invalid choice, please try again.")

#     conn.close()  # Close the connection when exiting

# if __name__ == '__main__':
#     main()










