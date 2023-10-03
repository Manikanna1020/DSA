import sys
import random 
from enum import Enum

def rps():
    
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input('\n Enter...\n 1 for Rock \n 2 for Paper \n 3 for Scissors: \n\n')
    
    if playerchoice not in ["1","2","3"]:
        print('pls enter 1, 2, or 3.')
        return rps()
        
    player =int(playerchoice)
    computerchoice = random.choice('123')
    computer = int(computerchoice)

    print('\nYou chose ' + str(RPS(player)).replace('rps.','').title() + '. ')
    print('\ncomputer chose ' + str(RPS(computer)).replace('rps.','').title() + '. ')

    if player == 1 and computer== 3 :
         print('\nYou win')
    elif player == 2 and computer ==1 :
         print('\nYou win')
    elif player ==3 and computer==2:
         print('\nYou win')
    elif player == computer:
         print('\nTie game')
    else:
         print('\nYou lose')

    print('\n Play Again')
    while True:
        playagain= input('\nY for Yes \nQ for Quit \n')
        if playagain.lower() not in ['y','q']:
         continue
        else:
          break
    if playagain.lower() == 'y':
        return rps()
    else:
        print('Thans for playing')
        sys.exit('\nsee u soon')
rps()
