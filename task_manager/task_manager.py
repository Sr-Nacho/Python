## Set up variables and library
# Import libraries and set up variables
import time
# Used to keep the while loop with the task manager inside active forever
active = True
# Creates an empty list to store tasks in
tasks = []
complete_tasks = []
report = 0
points = 0
ranks = []

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
    done_num = 0
    delete_num = 0
    
    # Determine how long the following loop will loop
    # This is considered home for the code
    # There are no task on the first execution, so the code will only let you enter tasks
    if len(tasks) == 0:   
        enter_bool = True
        done_bool = False
        delete_bool = False
        
    # Specifing between entering and deleting tasks
    # Default is delete
    else:
        
        enter_bool = input("Are you entering tasks? y/n ").lower() == "y"
        done_bool = input("Are you done with tasks? y/n ").lower() == "y"
        delete_bool = input("Are you deleting tasks? y/n ").lower() == "y"
        
    
    if enter_bool:
        task_num = int(input("How many tasks are you entering? "))
    if done_bool:
        done_num = int(input("How many tasks are you done with? "))
    if delete_bool:
        delete_num = int(input("How many tasks are you deleting? "))
    if not enter_bool and not done_bool and not delete_bool:
        print("None selected")
    
    # Input tasks
    
    for i in range(task_num):
        
        # Task input
        tasks.insert(i, input("Enter task " + str(i + 1) + " here "))
        
    if (done_bool or delete_bool) and enter_bool:
        print("New task list: ")
        # Prevent confusion by showing the user the new task order
        # Print tasks
        for i in range(len(tasks)):
            print("Task " + str(i + 1) + " " + tasks[i])
            time.sleep(1)
    
    
    # Finish tasks
    for i in range(done_num):
        done = int(input("Which task did you complete? Enter task number "))
        done -= 1
        complete_tasks.append(tasks[done])
        del tasks[done]
        points += 100
        print("Points = " + str(points))
        
        
    if delete_bool and done_bool:
        print("New task list: ")
        # Prevent confusion by showing the user the new task order
        # Print tasks
        for i in range(len(tasks)):
            print("Task " + str(i + 1) + " " + tasks[i])
            time.sleep(1)
            points -= 25
            print("Points = " + str(points))
        
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
        
    # Optional task display
    see_tasks = input("Would you like to see your tasks? y/n ").lower() == "y"
    if see_tasks:
        
        # Print tasks
        for i in range(len(tasks)):
            print("Task " + str(i + 1) + " " + tasks[i])
            time.sleep(1)
        if len(complete_tasks) > 0:
            print("Completed tasks: ")
            time.sleep(1)
            for i in range(len(complete_tasks)):
                print("Complete task " + str(i + 1) + " " + complete_tasks[i])
                time.sleep(1)
            
    print("Going home...")
    
    # Pause before sending back to home screen
    time.sleep(5)
    
    report += 1
    
## Used to identify errors
else: print("Something broke")
