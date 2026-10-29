import random

print("Welcome to the Tresure Hunt Game")


def tresure():
    tr=random.randint(0,4)
    tc=random.randint(0,4)
    return tr,tc

grid = []
def creategrid():
    for i in range(0,5):
        row = []
        for i in range(0,5):
            row.append("-")
        grid.append(row)
    return grid

def hint(tr,tc,row,col):
    if tr > row:
        return "The tresure is below"
    elif tr < row:
        return "The tresure is above"
    elif tc > col:
        return "The tresure is to the right"
    elif tc < col:
        return "The tresure is to the left"
    return "Congrtulations you found the tresure"


grid = creategrid()
tr1,tc1 = tresure()
attempts = 0
while True:
    for i in grid:
        print(" ".join(i))

    col = int(input("Choose a row(0-4): "))
    row = int(input("Choose a column(0-4): "))

    if tr1 == row and tc1 == col:
        print("You win")
        print("You have took {} to win".format(attempts))
        break

    else:
        print(hint(tr1,tc1,row,col)) 



