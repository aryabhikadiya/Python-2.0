phone_book = {}

while True:
    ans = input("\n\n1. Add contact \n2. Search contact \n3. Delete contact \n4. Exit\nEnter the number: ")
    if ans == "1":
        name = input("Enter the contact name: ").lower()
        number = input("Enter the phone number: ").lower()
        phone_book[name]=number
        print("Your contact has been added successfully.")

    elif ans == "2":
        search = input("Which contact name would you like to search for: ").lower()
        print()
        if search in phone_book:
            print("Contact found:", search)
        else:
            print("Contact not found.")

    elif ans == "3":
        delete = input("Which contact would you like to delete: ").lower()
        if delete in phone_book:
            phone_book.pop(delete)
            print(" {} has been successfully deleted from your phone book.".format(delete))
        else:
            print("Contact not found.")

    elif ans == "4":
        print("You have exited the app.")
        break

    else:
        print("Please enter a valid number!")