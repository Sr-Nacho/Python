## The actual project
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
achievement = []
streak = 0

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
            print("    Task " + str(i + 1) + " " + tasks[i])
            time.sleep(1)
    
    
    # Finish tasks
    for i in range(done_num):
        done = int(input("Which task did you complete? Enter task number "))
        done -= 1
        complete_tasks.append(tasks[done])
        del tasks[done]
        points += 100
        
    if delete_bool and done_bool:
        print("New task list: ")
        # Prevent confusion by showing the user the new task order
        # Print tasks
        for i in range(len(tasks)):
            print("    Task " + str(i + 1) + " " + tasks[i])
            time.sleep(1)
        
    # Delete tasks
    for i in range(delete_num):
        delete = int(input("Which task do you want to delete? Enter task number "))
        delete -= 1
        del tasks[delete]
        points -= 25
        
        # Prevent confusion by showing the user the new task order
        if delete_num > 1:
            print("New task list: ")
            
            # Print tasks
            for i in range(len(tasks)):
                print("    Task " + str(i + 1) + " " + tasks[i])
                time.sleep(1)
                
    print("Points = " + str(points))
        
    # Optional task display
    see_tasks = input("Would you like to see your tasks? y/n ").lower() == "y"
    if see_tasks:
        
        # Print tasks
        for i in range(len(tasks)):
            print("    Task " + str(i + 1) + " " + tasks[i])
            time.sleep(1)
        if len(complete_tasks) > 0:
            print("Completed tasks: ")
            time.sleep(1)
            for i in range(len(complete_tasks)):
                print("    Complete task " + str(i + 1) + " " + complete_tasks[i])
                time.sleep(1)
                
    report += 1
    
    # Achievements
    if "SSS+" in ranks and "Cheater" not in achievement:
        achievement.append("Cheater")
        print("""
            Achievement unlocked:
            
               >--Cheater--<
               
                   Cheat
            
            """)
    if "SSS" in ranks and "Max Power" not in achievement:
        achievement.append("Max power")
        print("""
            Achievement unlocked:
            
               >--Max Power--<
                   
               Reach SSS rank
        
        """)
    if points < 0 and report == 5 and "Sub-Zero" not in achievement:
        achievement.append("Sub-Zero")
        print("""
            Achievement unlocked:
            
                >--Sub-Zero--<
                
                Get a negative 
                score. It's cold,
                but fair
                
        """)
    if "F" in ranks and "D" in ranks and "C" in ranks and "B" in ranks and "A" in ranks and "S" in ranks and "SS" in ranks and "SSS" in ranks and "I've seen it all" not in achievements:
        achievement.append("I've seen it all")
        print("""
            Achievement unlocked:
            
           >--I've seen it all--<
           
               Get all of the
               ranks
               
        """)
    if streak == 5 and "Streak" not in achievements:
        print("""
            Achievement unlocked:
                
                >--Streak--<
                
                Get B rank or
                higher 5 times
                in a row
                
        """)
    if rank == "A" and "Ace" not in achievements:
        print("""
            Achievement unlocked:
            
                >--Ace--<
                
                Get an A
                rank
        """)
                
    # Progress reports
    if report == 5:
        report = 0
        if points < 100:
            rank = "F"
            print("Rank " + rank)
            streak = 0
        elif points <= 200:
            rank = "D"
            print("Rank " + rank)
            streak = 0
        elif points <= 300:
            rank = "C"
            print("Rank " + rank)
            streak = 0
        elif points <= 400:
            rank = "B"
            print("Rank " + rank)
            streak += 1
        elif points <= 550:
            rank = "A"
            print("Rank " + rank)
            streak += 1
        elif points <= 750:
            rank = "S"
            print("Rank " + rank)
            streak += 1
        elif points <= 1000:
            rank = "SS"
            print("Rank " + rank)
            streak += 1
        elif points > 1000:
            rank = "SSS"
            print("Rank " + rank)
            streak += 1
        else:
            # You have to cheat to get this
            rank = "SSS+"
            
        ranks.append(rank)
        points = 0
    
    print("Going home...")
    
    # Pause before sending back to home screen
    time.sleep(5)
    
# Used to identify errors
# Since the while loop never ends, the else will never run
else: print("Something broke")
