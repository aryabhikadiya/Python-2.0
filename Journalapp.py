import time

while True:
    ans = input("\n1.Add Entry \n2.View Entry \n3.Exit \nPlease select a number:")

    if ans == "1":
        add = input("Please enter an Entry: ")
        with open("Journal.txt","a")as store:
            store.write("\n" + add)
        print("{} has been saved".format(add))
        
    
        