"""
Unit 1
Code Your Own: Unit 1
Task Reminder
"""
## Get inputs ##

# Task 1 input #
task1 = input("What Is your first task? ").lower()

goal1 = int(input("How many times do you want to do this? "))

task_check = input("Is that all of the tasks?(max 3 tasks) ").lower()

tasks = 1

# Check for other tasks #
while(task_check == 'no'):
    
    # Task 2 input #
    task2 = input("What Is your second task? ").lower()
    
    goal2 = int(input("How many times do you want to do this? "))
    
    task_check = input("Is that all of the tasks?(max 3 tasks) ").lower()
    
    tasks = 2
    
    # Check for other tasks #
    while(task_check == 'no'):
        
        # Task 3 input #
        task3 = input("What Is your third task? ").lower()

        goal3 = int(input("How many times do you want to do this? "))

        print('That is all of the tasks I can handle. ')
        
        task_check = 'yes'
        
        tasks = 3
        
    else:
        print('')

else:
    print('')
    
## Print tasks + get task number input ##
x1 = 0
while x1 == 0:

    if tasks == 1:
        task1_num = int(input('How many times have you completed the task? '))
        remaining1 = goal1 - task1_num
        if remaining1 < 0:
            print('You went above and beyond, well done!')
            
        else:
            print('You have done ' + task1 + ' ' + str(task1_num) + ' times')
            print('only ' + str(remaining1) + ' more times')
            
    elif tasks == 2:
        
        task1_num = int(input('How many times have you completed the first task? '))
        remaining1 = goal1 - task1_num
        if remaining1 < 0:
            print('You went above and beyond, well done!')
            
        else:
            print('You have done ' + task1 + ' ' + str(task1_num) + ' times')
            print('only ' + str(remaining1) + ' more times')
            
        task2_num = int(input('How many times have you completed the second task? '))
        remaining2 = goal2 - task2_num
        if remaining2 < 0:
            print('You went above and beyond, well done!')
           
        else:
            print('You have done ' + task2 + ' ' + str(task2_num) + ' times')
            print('only ' + str(remaining1) + ' more times')
    elif tasks == 3:
        
        task1_num = int(input('How many times have you completed the first task? '))
        remaining1 = goal1 - task1_num
        if remaining1 < 0:
            print('You went above and beyond, well done!')
            
        else:
            print('You have done ' + task1 + ' ' + str(task1_num) + ' times')
            print('only ' + str(remaining1) + ' more times')
        
        task2_num = int(input('How many times have you completed the second task? '))
        remaining2 = goal2 - task2_num
        if remaining2 < 0:
            print('You went above and beyond, well done!')
            
        else:
            print('You have done ' + task2 + ' ' + str(task2_num) + ' times')
            print('only ' + str(remaining1) + ' more times')
        
        task3_num = int(input('How many times have you completed the third task? '))
        remaining3 = goal3 - task3_num
        if remaining3 < 0:
            print('You went above and beyond, well done!')
            
        else:
            print('You have done ' + task3 + ' ' + str(task3_num) + ' times')
            print('only ' + str(remaining3) + ' more times')
    print()
    end = input('Should i end the program here?(yes/no) ').lower()
    if end == "yes":
        x1 = 3
    print()
## Check for errors, be sure the code ran sucessfully, and prevent infinite loops ##

task_check = 'yes'

print('Code complete')
