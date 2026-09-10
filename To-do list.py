task = []
while True:
    print("1. View your tasks\n2. Add task \n3. Remove task \n4. Exit")
    num = int(input("Enter a number:"))
    if num == 1: 
        for i in task:
            
            print(i)

    elif num == 2:
        add = input("Add a task:")
        task.append(add)
        print("This task has been added")

    elif num == 3:
        rem = input("Remove a task:")
        task.remove(rem)
        print("This task has been removed")

    elif num == 4:
        print("You have exitied the app. BYE!")
        break

    else:
        print("Please select a number between 1-4")

    

    

    


        
    



