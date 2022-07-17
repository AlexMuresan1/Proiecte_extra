import random

n=3
b=random.randint(1,10)
corect=1
while n>0:
    print("You have",n,"more tries!")
    a=int(input("Enter a number between 1 and 10:"))

    if a==b:
        corect=1
        print("You guessed the correct number!")
        break
    else:
        n=n-1
        corect=0
        print("Your number is not correct! Try again")
if corect==0:
    print()
    print("You couldn't guessed the correct number! The correct number was",b)


