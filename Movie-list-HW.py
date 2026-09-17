movies = []

while True:
    print("1. View Movies\n2. Add a movie\n3. Remove a movie\n4. Exit")
    num = int(input("Enter a number:"))
    if num == 1: 
        for i in movies:
            
            print(i)

    elif num == 2:
        add = input("Add a movie:")
        movies.append(add)
        print("This movie has been added")

    elif num == 3:
        rem = input("Remove a movie:")
        movies.remove(rem)
        print("This movie has been removed")

    elif num == 4:
        print("You have exitied the app. BYE!")
        break

    else:
        print("Please select a number between 1-4")