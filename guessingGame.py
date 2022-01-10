import random
number = random.randint(1, 9)
chanceCount = 0
while (chanceCount < 5):
    introString = int(input("Choose a number between 1-9: "))
    if (introString > number):
        print("Your guess is too big")
    elif (introString == number):
        print("Congratulation! You guessed it correct")
    else :
        print("Your number guess is too less")
    chanceCount = chanceCount + 1
if (chanceCount > 5):
    print("You lost! The number is")
    print(number)