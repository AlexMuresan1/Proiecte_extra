import random

l=int(input("Enter the password length(has to be 8 or more characters!): "))
pw=""
sl=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
bl=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n=[1,2,3,4,5,6,7,8,9,0]

#first character is big letter
pw+=random.choice(bl)

#next three has to be numbers
for i in range(0,3):
    pw+=str(random.choice(n))

#next has to be small letters
x=l-4
for i in range(0,x):
    pw+=random.choice(sl)

print("Generated password is: ",pw)


    
