import random

print(" Welcome to Number Guessing Game")
print("Guess Any number from 1 to 9 ")

number = random.randint(1,9)
chances = 1

while chances < 5:
    guess = input(" Guess correct number : ")
    chances = chances + 1
    if guess == number:
     print("Congratulations You have WON THE GAME !!! ")
     break

if not chances <5 :
    print("You have lost the game !!, The number is :",number)


    
    

    


