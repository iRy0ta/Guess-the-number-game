import random

while True:
    min = input("Enter the minimum number:")
    if(not(min.isdigit())):
        print("Please Enter integer")
        continue

    max = input("Enter the maximum number:")
    if(not(max.isdigit())):
        print("Please Enter integer")
        continue

    if(min < max): break
    else: print("Please enter the maximum number that is bigger than the minimum number")

rand = random.randint(int(min), int(max))

for i in range(5):
    guessNumber = input("Enter your guess number:")

    if(int(guessNumber) == rand):
        print("Your guess is correct!")
        break
    
    if(i == 4): print("Game Over")
