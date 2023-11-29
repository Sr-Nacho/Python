## Set up variables and library
# Import libraries and set up variables
import time
# Used to keep the while loop with the task manager inside active forever
active = True
# Creates an empty list to store tasks in
tasks = []

# Welcome the user with a start message
# The user should only see the start message once
print("Hi, welcome to the task manager")
# Use pauses to create a feeling simmilar to that of fake loading screens
time.sleep(1)

## Main body of the code
# This is the part of the code that is used the whole time
# When the end is reached, it starts over again until the app is closed
while active:
    
    # Reseting options
    task_num = 0
    delete_num = 0
    
    # Determine how long the following loop will loop
    # This is considered home for the code
    # There are no task on the first execution, so the code will only let you enter tasks
    if len(tasks) == 0:   
        enter = True
        
    # Specifing between entering and deleting tasks
    # Default is delete
    else:
        enter = input("Are you entering or deleting tasks? enter/delete ").lower() == "enter"
        
    if enter:
        task_num = int(input("How many tasks are you entering? "))
    else:
        delete_num = int(input("How many tasks are you deleting? "))
    
    # Delete tasks
    for i in range(delete_num):
        delete = int(input("Which task do you want to delete? Enter task number "))
        delete -= 1
        del tasks[delete]
        
        # Prevent confusion by showing the user the new task order
        if delete_num > 1:
            print("New task list: ")
            
            # Print tasks
            for i in range(len(tasks)):
                print("Task " + str(i + 1) + " " + tasks[i])
                time.sleep(1)
    
    # Input tasks
    for i in range(task_num):
        
        # Task input
        tasks.insert(i, input("Enter task " + str(i + 1) + " here "))
        
    # Optional task display
    see_tasks = input("Would you like to see your tasks? y/n ").lower() == "y"
    if see_tasks:
        
        # Print tasks
        for i in range(len(tasks)):
            print("Task " + str(i + 1) + " " + tasks[i])
            time.sleep(1)
    print("Going home...")
    
    # Pause before sending back to home screen
    time.sleep(5)
    
## Used to identify errors
else: print("Something broke")
