
from random import randint
# 1. Random a number

numb = randint(0,100)
print(numb)

playing = True
count = 0
while playing: 
    # 2. Input, lap lai 2 va 3

    
    if count >=7:
        print('You lose :<')
        playing = False
    else: 
        guess = int(input("Guess my number (0-100) "))

    # 3. Verifying
    if guess > numb:
        print("A little too large :( ")
    elif guess < numb:
        print('Too small :(')
    else:
        print('Bingo')
        playing = False
    count += 1
    
# Doan toi da 7 lan, tao bien dem so lan doan
# loops = True

# while loops:

#     
#     if yn == numb:
#         print('Bingo')
#     else:
#         print('Guess again')





