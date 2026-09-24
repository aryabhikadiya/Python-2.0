dic = {}

while True:
    ans = input("1. Add/Update a word \n2. Retrive a words definition \n3. Delete a word \n4. View all words \n5. Exit\nEnter the number:")
    if ans == "1":
        word = input("Enter the word you would like to add: ")
        defi = input("Enter the definition of the word: ")
        dic[word]=defi
        print("Your word has been added/updated succesfully")





