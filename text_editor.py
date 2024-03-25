# It's totally broken but i didn't even steal it
# Unless you want an error log database, delete the sql bits
import tkinter as tk
from tkinter import filedialog
import subprocess
from time import ctime
import sqlite3
import time
import os

log = []

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            text = text_editor.get("1.0", tk.END)
            file.write(text)

def encrypt_with_kleopatra(file_path):
    try:
        # Use subprocess to call Kleopatra
        print("Encrypting file:", file_path)  # Print the file path before encryption
        subprocess.run(["kleopatra", "--encrypt", file_path], check=True)
        print("File encrypted successfully with Kleopatra.")
    except Exception as e:
        # Record the error along with the timestamp
        error_time = time.ctime()
        log_error_to_database(str(e), error_time)
    
        # Display data from the log list
        print("Data from log list:")
        for error_entry in log:
            print(error_entry)

# Define a function to log errors to both the SQL database and the log list
def log_error_to_database(error_message, error_time):
    # Log error to the log list
    log.append((error_message, error_time))
    
    # Log error to the SQL database
    cursor.execute('INSERT INTO errors (error_message, error_time) VALUES (?, ?)', (error_message, error_time))
    conn.commit()

# Display data from the SQL database
def display_database():
    cursor.execute('SELECT * FROM errors')
    database_errors = cursor.fetchall()
    print("\nData from SQL database:")
    for database_entry in database_errors:
        print(database_entry)

# Command to clear the SQL database
def clear_database():
    cursor.execute('DELETE FROM errors')
    conn.commit()
    print("Database cleared successfully.")

# Create the main window
root = tk.Tk()
root.title("Simple Text Editor")

# Create a text widget
text_editor = tk.Text(root)
text_editor.pack()

# Create a "Save" button
save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack()

# Run the application
root.mainloop()

# Create a connection to the SQLite database
conn = sqlite3.connect('error_log.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store errors if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS errors
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                error_message TEXT,
                error_time TEXT)''')

try:
    file_path = input("Insert file path here: ")
    
    # Normalize the file path to ensure correct formatting
    file_path = os.path.normpath(file_path)
    
    print("Normalized file path:", file_path)  # Print the normalized file path
    file_to_encrypt = file_path
    encrypt_with_kleopatra(file_to_encrypt)
except Exception as e:
    # Record the error along with the timestamp
    error_time = time.ctime()
    log_error_to_database(str(e), error_time)

    # Display data from the log list
    print("Data from log list:")
    for error_entry in log:
        print(error_entry)

finish_instruct = input("S to see all errors, C to clear all error logs: ").lower()
if finish_instruct == "c":
   # Clear the SQL database
    clear_database()
elif finish_instruct == "s":
    # Display data from the SQL database
    display_database()

# Close the cursor and connection to the database
cursor.close()
conn.close()
