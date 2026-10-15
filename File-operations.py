#Open the file in write mode
store = open("document.txt","w")

#Write in the file
store.write("My name is Arya")
store.write("\nI am 13 years old")
store.close()

#Opening the file in read mode
store = open("document.txt","r")

#Read the contents from the file
print (store.read())
store.close()

store = open("document.txt","r")
print (store.readline())
store.close()

#Opening the file in append mode
store = open("document.txt","a")
store.write("\nI am from India")
store.close()

#Opening the file in wirte mode using with open
with open("words.txt","w")as store:
    store.write("My hobbies are: ")

with open("words.txt","a")as store:
    store.write("\ncricket")

with open("words.txt","r")as store:
    print (store.read())

with open("words.txt","r")as store:
    print (store.readline())
    




