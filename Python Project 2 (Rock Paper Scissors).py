import random
d = {'rock': 1, 'paper': 2, 'scissors': 3}
rd = {1: 'rock', 2: 'paper', 3: 'scissors'}

computer = random.randint(1, 3)


def start():
    number = input("Which one do you want to choose?\nRock, paper, or scissors?\n").lower()
    human = (d[number])
    computer1 = rd[computer]
    print("computer put",  computer1)
    if computer == human:
        print("It is a tie")
    elif computer == 1 and human == 3:
        print("Computer wins")
    elif computer == 1 and human == 2:
        print("Human wins")
    elif computer == 2 and human == 1:
        print("Computer wins")
    elif computer == 2 and human == 3:
        print("Human wins")
    elif computer == 3 and human == 1:
        print("Human wins")
    elif computer == 3 and human == 2:
        print("Computer wins")


start()