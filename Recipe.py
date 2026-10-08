

while True:
    recipe = input("\n1. Convert Cups to Grams \n2. Grams to Cups \n3. Tablespoons to Teaspoons \n4. Teaspoons to Tablespoons \n5. Exit \nEnter a number between 1-5: ")

    if recipe == "1":
        cups = int(input("How many cups: "))
        grams = int(input("How many grams in a cup: "))
        ans = cups*grams
        print(ans)

    elif recipe == "2":
        grams = int(input("How many grams: "))
        cups = int(input("How many cups per gram: "))
        ans = grams/cups
        print(ans)
    
    elif recipe == "3":
        table = int(input("How many Tablespoons do you have: "))
        ans = table*3
        print(ans)        

    elif recipe == "4":
        tea = int(input("How many Teaspoons do you have: "))
        ans = tea/3
        print(ans) 

    elif recipe == "5":
        print("You have exitied the app. GOODBYE!")
        break

    else:
        print("You have entered something invalid!")
        
    
    

