import random
number = random.randint(1,100)
player_name = input(' Hello, what is your name? ')
a = 0
print('Hi'+player_name+'! I am guessing a number between 1 and 100;')
while True:
    a+=1
    guess = int(input(" Guess the number "))
    if number ==guess:
        print ("You found the correct number, Good job!!!")
        print(f"It took you {a} rounds.")
        break
    elif guess - number>35 or number - guess >35:
        print("VERY COLD")
    elif guess - number>20 or number - guess >20:
        print("COLD")
    elif guess - number>5 or number - guess >5:
        print("HOT")
    elif guess - number>1 or number - guess >1:
        print("VERY HOT")
    else:
        pass