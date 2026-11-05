import random
games = ["minecraft","fortnite","call_of_duty","roblox","rocket_league","fc27","tennis_clash","among_us","rainbow_six_seige"]

print("Welcome to the scramble game. Good luck!")
levels = 5

def scramble(word):
    words = list(word)
    random.shuffle(words)
    return "".join(words)

for i in range(1, levels + 1):
    game = random.choice(games)
    scramabled_word = scramble(game)
    print("\nThis is the {} scrambled word".format(scramabled_word))
    hint = input("Do you want a hint. Yes or no:").lower()
    if hint == "yes":
        print(game[0])
    ans = input("What do you think is the word: ").lower()
    if ans == game:
        print("You have guessed the word correctly!")
    else:
        print("Your answer is wrong. The correct answer is {}".format(game))

    


