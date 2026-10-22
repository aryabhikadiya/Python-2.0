import time

while True:
    ans = input("\n1.Add Entry \n2.View Entry \n3.Exit \nPlease select a number:")

    if ans == "1":
        add = input("Please enter an Entry: ")
        with open("Journal.txt","a")as store:
            store.write("\n" + add)
        print("{} has been saved".format(add)) 


    elif ans == "2":
        with open("Journal.txt","r")as store:
            print (store.read())
            
        

    elif ans == "3":
        print("You have exitied the journal app. Bye!")
        break

    else: 
        print("Enter something valid")


    



        
    
        