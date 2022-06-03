import random

from click import option

options = {'R': 'Rock', 'P': 'Paper', 'S': "Scissors"}
print("""
    This is a Rock Paper Scissors game.
    'R' means Rock, 'P' means paper and 'S' means scissors
    Rock beats Scissors
    Paper beats Rock 
    Scissors beats Paper
    pick an option between "R", "P" or "S"
""")
while True:

    try:
        player =  input('Enter option: ')
        computer = random.choice(list(options))
        print(f'Player ({options[player]}): CPU ({options[computer]})')
        if player == computer:
            print("it's a tie")
            continue
        else:
            if player == 'R' and computer == 'S':
                print("Rock beats Scissors, You Won")
            elif player == 'S' and computer == 'R':
                print ("Rock beats Scissors, You Lost""")
            elif player == 'P' and computer == 'R':
                print("Paper beats Rock, You Won""")
            elif player == 'R' and computer == 'P':   
                print("Paper beats Rock, You Lost""")
            elif player == 'S' and computer == 'P':
                print("Scissors beats Paper, You Won""")
            else:
                print("Scissors beats Paper, You Lost""")
            break
    except KeyError:
        print ("Not amongst our options. \n pick an option between 'R', 'P' or 'S'.")
        continue
