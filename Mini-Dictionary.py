dic = {}

while True:
    ans = input("\n\n1. Add/Update a word \n2. Retrive a words definition \n3. Delete a word \n4. View all words \n5. Exit\nEnter the number:")
    if ans == "1":
        word = input("Enter the word you would like to add: ").lower()
        defi = input("Enter the definition of the word: ").lower()
        dic[word]=defi
        print("Your word has been added/updated succesfully")

    elif ans == "2":
        retrive = input("Which word would you like to retrive the definition of: ").lower()
        print()
        print(dic[retrive])

    elif ans == "3":
        delete = input("which word would you like to delete: ").lower()
        dic.pop(delete)
        print(" {} has been succefully deleted for your dictionary".format(delete))

    elif ans == "4":
        if dic :
            for i in dic:
                print("{}:{}".format(i,dic[i]))

        else:
            print("Your dictionary is currently empty")
            

    elif ans == "5":
        print("You have exitied the app")
        break

    else:
        print("Please enter a valid number!")
        









