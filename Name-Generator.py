import random


while True:
    name = input("Please enter your full name:(enter 'exit' to leave)")
    if name == "exit":
        print("You have exitied, Bye!")
        break
    sepname = name.split()
    if len(sepname)<2:
        print("Please enter your full name(including first and last name)")
        continue
    firstname = sepname[0]
    lastname = sepname[1]
    user1 = firstname[0:3] + lastname[0:3] + str(random.randint(20,60))
    user2 = firstname + str(random.randint(50,500))
    user3 = lastname + str(random.randint(50,500))
    user4 = firstname[-3:] + lastname[0:3] + str(random.randint(10,300))
    user5 = firstname[-2:] + lastname[-2:] + str(random.randint(1000,2000))

    username = [user1, user2, user3, user4, user5]
    usernames = random.choice(username)

    print (usernames)
    



