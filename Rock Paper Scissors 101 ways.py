import random

choices = []
for a in range(101):
    choices.append(a)



status = ''
wins = 0
draws = 0
losts = 0
while status.lower() != 'quit':
    CPU_Choice = random.randint(0, len(choices))
    Player_Choice = input("What do you choose? ")
    
    #Find player_choice str in array
    Player_Choice = int(Player_Choice)

    print("CPU chose:", choices[CPU_Choice])
    Player_Win_Option = Player_Choice + (len(choices)-1)/2

    Player_Status = 'won'
    if CPU_Choice < Player_Choice:
        Player_Status = 'lost'
    if (CPU_Choice - (len(choices)-1)/2) > Player_Choice:
        Player_Status = 'lost'
    if Player_Win_Option > (len(choices)-1) and CPU_Choice < (Player_Win_Option - len(choices) - 1):
        Player_Status = 'won'
    if Player_Win_Option == CPU_Choice:
        Player_Status = 'drew'

    if Player_Status == 'won':
        wins += 1
    elif Player_Status == 'lost':
        losts += 1
    elif Player_Status == 'drew':
        draws += 1
    else:
        print('error')
    
    print("You...", Player_Status, "\n \nCurrent stats: \nWins:", wins, "\nDraws:", draws, "\nLosts:", losts)
    status = input("\nWould you like to play again? (Yes/Quit) ")



1
l L
i I

