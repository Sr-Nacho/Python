## The actual project
## Set up variables and library
# Import libraries and set up variables
import time
# Creates all of the variables we will need
active = True
tasks = []
complete_tasks = []
report = 0
points = 0
ranks = []
achievement = []
streak = 0
rank = " "
perm_rank_points = 0
perm_rank = "None"

# Welcome the user with a start message
# The user should only see the start message once
print("""
Hi, welcome to the task manager.
Do tasks to get points. More points
equals a higher rank. You have a rank
given periodically, that is temporary.
It represents your productivity in the
moment. You have another rank that is 
increased by consistently getting a good
temporary rank. This rank is permanent,
and shows your consistency over time.
Achievements are one time goals that show
your peak productivity and what you have done
over time.
""")
# Use pauses to create a feeling simmilar to that of fake loading screens
time.sleep(10)

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
        points += 150
        
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
        points -= 50
        
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
    # These achievements are not meant to be easy
    # You should not be getting an A rank often, making the achievement worth while
    # This achievement should be impossible to get
    if "SSS+" in ranks and "Cheater" not in achievement:
        achievement.append("Cheater")
        print("""
            Achievement unlocked:
            
               >--Cheater--<
               
                   Cheat
            
            """)
    # This achievement marks great effort, and is a major step
    if "SSS" in ranks and "Max Power" not in achievement:
        achievement.append("Max power")
        print("""
            Achievement unlocked:
            
               >--Max Power--<
                   
               Reach SSS rank
        
        """)
    # This is our version of a participation award
    if points < 0 and report == 5 and "Sub-Zero" not in achievement:
        achievement.append("Sub-Zero")
        print("""
            Achievement unlocked:
            
                >--Sub-Zero--<
                
                Get a negative 
                score. It's cold,
                but fair
                
        """)
    # The hardest possible achievement
    # Uses nested if statements to keep the line short, since it was over the limit for PEP-8
    if "F" in ranks:
        if "D" in ranks:
            if "C" in ranks:
                if "B" in ranks:
                    if "A" in ranks:
                        if "S" in ranks:
                            if "SS" in ranks:
                                if "SSS" in ranks: 
                                    if "I've seen it all" not in achievements:
                                        achievement.append("I've seen it all")
                                        print("""
                                            Achievement unlocked:

                                           >--I've seen it all--<

                                               Get all of the
                                               ranks

                                        """)
    # Meant to show consistency
    if streak == 5 and "Streak" not in achievements:
        achievement.append("Streak")
        print("""
            Achievement unlocked:
                
                >--Streak--<
                
                Get B rank or
                higher 5 times
                in a row
                
        """)
    # Get an achievement every time you hit a new rank
    if (rank == "S" or rank == "SS" or rank == "SSS") and "Super" not in achievements:
        achievement.append("Super")
        print("""
            Achievement unlocked:
            
                >--Super--<
                
                Get S rank 
                or higher
                
        """)
    if rank == "A" and "Ace" not in achievements:
        achievement.append("Ace")
        print("""
            Achievement unlocked:
            
                >--Ace--<
                
                Get an A
                rank
                
        """)
    if rank == "B" and "Ballin'" not in achievements:
        achievement.append("Ballin'")
        print("""
            Achievement unlocked:
            
               >--Ballin'--<
                
                Get a B
                rank
                
        """)
    if rank == "C" and "C-uperior" not in achievements:
        achievement.append("C-uperior")
        print("""
            Achievement unlocked:
            
               >--C-uperior--<
                
                Get a C
                rank
                
        """)
    if rank == "D" and "Doing something" not in achievements:
        achievement.append("Doing something")
        print("""
            Achievement unlocked:
            
            >--Doing something--<
                
                Get a D
                rank
                
        """)
    if rank == "F" and "We all start somewhere" not in achievements:
        achievement.append("We all start somewhere")
        print("""
            Achievement unlocked:
            
         >--We all start somewhere--<
                
                Get a F
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
            
        # Permanent ranks
        # Progression is meant to slow to a crawl the higher you get
        # Elite might take lots of time to become champion with SSS, so it shows consistency
        # This part adds/subtracts points
        # It also runs only when the temporary ranks are evaluated

        if perm_rank == "None":
            if rank == "F":
                perm_rank_points += 0
            elif rank == "D":
                perm_rank_points += 10
            elif rank == "C":
                perm_rank_points += 25
            elif rank == "B":
                perm_rank_points += 50
            elif rank == "A":
                perm_rank_points += 100
            elif rank == "S":
                perm_rank_points += 250
            elif rank == "SS":
                perm_rank_points += 500
            elif rank == "SSS":
                perm_rank_points += 1000
        if perm_rank == "Stone":
            if rank == "F":
                perm_rank_points -= 10
            elif rank == "D":
                perm_rank_points += 0
            elif rank == "C":
                perm_rank_points += 10
            elif rank == "B":
                perm_rank_points += 25
            elif rank == "A":
                perm_rank_points += 50
            elif rank == "S":
                perm_rank_points += 100
            elif rank == "SS":
                perm_rank_points += 250
            elif rank == "SSS":
                perm_rank_points += 500
        if perm_rank == "Bronze":
            if rank == "F":
                perm_rank_points -= 25
            elif rank == "D":
                perm_rank_points -= 10
            elif rank == "C":
                perm_rank_points += 0
            elif rank == "B":
                perm_rank_points += 10
            elif rank == "A":
                perm_rank_points += 25
            elif rank == "S":
                perm_rank_points += 50
            elif rank == "SS":
                perm_rank_points += 100
            elif rank == "SSS":
                perm_rank_points += 250
        if perm_rank == "Silver":
            if rank == "F":
                perm_rank_points -= 50
            elif rank == "D":
                perm_rank_points -= 25
            elif rank == "C":
                perm_rank_points -= 10
            elif rank == "B":
                perm_rank_points += 0
            elif rank == "A":
                perm_rank_points += 10
            elif rank == "S":
                perm_rank_points += 25
            elif rank == "SS":
                perm_rank_points += 50
            elif rank == "SSS":
                perm_rank_points += 100
        if perm_rank == "Gold":
            if rank == "F":
                perm_rank_points -= 100
            elif rank == "D":
                perm_rank_points -= 50
            elif rank == "C":
                perm_rank_points -= 25
            elif rank == "B":
                perm_rank_points -= 10
            elif rank == "A":
                perm_rank_points += 0
            elif rank == "S":
                perm_rank_points += 10
            elif rank == "SS":
                perm_rank_points += 25
            elif rank == "SSS":
                perm_rank_points += 50
        if perm_rank == "Diamond":
            if rank == "F":
                perm_rank_points -= 250
            elif rank == "D":
                perm_rank_points -= 100
            elif rank == "C":
                perm_rank_points -= 50
            elif rank == "B":
                perm_rank_points -= 25
            elif rank == "A":
                perm_rank_points -= 10
            elif rank == "S":
                perm_rank_points += 0
            elif rank == "SS":
                perm_rank_points += 10
            elif rank == "SSS":
                perm_rank_points += 25
        if perm_rank == "Elite":
            if rank == "F":
                perm_rank_points -= 500
            elif rank == "D":
                perm_rank_points -= 250
            elif rank == "C":
                perm_rank_points -= 100
            elif rank == "B":
                perm_rank_points -= 50
            elif rank == "A":
                perm_rank_points -= 25
            elif rank == "S":
                perm_rank_points -= 10
            elif rank == "SS":
                perm_rank_points += 0
            elif rank == "SSS":
                perm_rank_points += 10
        if perm_rank == "Champion":
            if rank == "F":
                perm_rank_points -= 1000
            elif rank == "D":
                perm_rank_points -= 500
            elif rank == "C":
                perm_rank_points -= 250
            elif rank == "B":
                perm_rank_points -= 100
            elif rank == "A":
                perm_rank_points -= 50
            elif rank == "S":
                perm_rank_points -= 25
            elif rank == "SS":
                perm_rank_points -= 10
            elif rank == "SSS":
                perm_rank_points += 0
        
        # Decide/display permanent rank
        # Points required decreases as rank increases
        if perm_rank_points < 0:
            perm_rank_points = 0
        if perm_rank_points > 0:
            perm_rank = "Stone"
            print("Stone rank")
            print(str(perm_rank_points) + " points")
        if perm_rank_points <= 200:
            perm_rank = "Bronze"
            print("Bronze rank")
            print(str(perm_rank_points) + " points")
        if perm_rank_points <= 600:
            perm_rank = "Silver"
            print("Silver rank")
            print(str(perm_rank_points) + " points")
        if perm_rank_points <= 900:
            perm_rank = "Gold"
            print("Gold rank")
            print(str(perm_rank_points) + " points")
        if perm_rank_points <= 1100:
            perm_rank = "Diamond"
            print("Diamond rank")
            print(str(perm_rank_points) + " points")
        if perm_rank_points <= 1300:
            perm_rank = "Elite"
            print("Elite rank")
            print(str(perm_rank_points) + " points")
        if perm_rank_points <= 1500:
            perm_rank = "Champion"
            print("Champion rank")
            print(str(perm_rank_points) + " points")

        ranks.append(rank)
        points = 0
    
    print("Going home...")
    
    # Pause before sending back to home screen
    time.sleep(5)
    
## Used to identify errors
else: print("Something broke")
