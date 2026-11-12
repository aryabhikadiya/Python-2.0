import random
games = ["minecraft","fortnite","call of duty","roblox","rocket league","fc27","tennis clash","among us","rainbow six seige"]
print("WELCOME TO THE HANG-MAN GAME")
attempts = 5

game = random.choice(games)
dash = ["_"]*len(game)

print(" ".join(dash))
while attempts >0 and "_" in dash:
    letter = input("Guess a letter: ")
    if letter in game:
        print("You have guessed the correct letter")
        for i in range(len(game)):
            if game [i]==letter:
                dash[i]=letter
        

    else:
        print("You have guessed it incorrectly.")
        attempts = attempts - 1
        print("You have {} left".format(attempts))

    print(" ".join(dash)) 

if "_" not in dash:
    print("Congrats, You have won!")

else:
    print("You have lost. Better luck next time")

