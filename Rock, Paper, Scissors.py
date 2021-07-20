from random import randint
player = input('Rock (r), Paper (p), or Scissors (s)?: ')
print (player, 'vs', end=' ')

chosen = randint(1,3)

if chosen == 1:
    computer = 'r'

elif chosen == 2:
    computer = 'p'

else:
    computer = 's'
print(computer)

if player == computer:
    print('TIE!')
    
elif player == 'r' and computer == 's':
    print('Congrats, You Won! ')    

elif player == 'r' and computer == 'p':
    print('Sadly, the Computer Won.')

elif player == 'p' and computer == 'r':
    print('Congrats, You Won! ')

elif player == 'p' and computer == 's':
    print('Sadly, the Computer Won.')

elif player == 's' and computer == 'p':
    print('Congrats, You Won! ')

elif player == 's' and computer == 'r':
    print('Sadly, the Computer Won.')
