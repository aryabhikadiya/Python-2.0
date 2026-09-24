import random

name = input("Please enter your full name:(enter 'exit' to leave)")
if name == "exit":
    print("You have exitied, Bye!")
    exit()
sepname = name.split()
if len(sepname)<2:
    print("Please enter your full name(including first and last name)")
    exit()
firstname = sepname[0]
lastname = sepname[1]

ticket_code = firstname[0:2] + lastname[-3:] + str(random.randint(100, 999))

print(ticket_code)