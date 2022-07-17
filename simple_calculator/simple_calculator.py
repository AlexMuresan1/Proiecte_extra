import math


print("press '+' to add 2 numbers")
print("press '-' to substract 2 numbers")
print("press '*' to multiply 2 numbers")
print("press '/' to divide 2 numbers")
print("press 'r' to know the radical of a number")
print("press '^2' to exponentiate a number by 2")
print("press '^n' to exponentiate a number by another number")


while True:
    option = input("the option is:")
    if option=="+":
        a=float(input("Introduce first number:"))
        b = float(input("Introduce second number:"))
        print("The sum of",a,"and",b,"is:",a+b)
        r=input("Do you want to continue with another operation?")
        if r=="n" or r=="no" or r=="NO" or r=="No":
            break
    elif option=="-":
        a = float(input("Introduce first number:"))
        b = float(input("Introduce second number:"))
        print("The substraction of", a, "and", b, "is:", a - b)
        r = input("Do you want to continue with another operation?")
        if r == "n" or r == "no" or r == "NO" or r == "No":
            break
    elif option=="*":
        a = float(input("Introduce first number:"))
        b = float(input("Introduce second number:"))
        print("The multiplication of", a, "and", b, "is:", a*b)
        r = input("Do you want to continue with another operation?")
        if r == "n" or r == "no" or r == "NO" or r == "No":
            break
    elif option=="/":
        a = float(input("Introduce first number:"))
        b = float(input("Introduce second number:"))
        print("The division of", a, "and", b, "is:", a/b)
        r = input("Do you want to continue with another operation?")
        if r == "n" or r == "no" or r == "NO" or r == "No":
            break
    elif option=="r":
        a=float(input("Introduce the number:"))
        print("The radical of number",a,"is:",math.sqrt(a))
        r = input("Do you want to continue with another operation?")
        if r == "n" or r == "no" or r == "NO" or r == "No":
            break
    elif option=="^2":
        a = float(input("Introduce the number:"))
        print("The number raised to the power 2 is:",math.pow(a,2))
        r = input("Do you want to continue with another operation?")
        if r == "n" or r == "no" or r == "NO" or r == "No":
            break
    elif option=="^n":
        a=float(input("Introduce the base:"))
        b=float(input("Introduce the exponent:"))
        print("The number",a,"raised at the power",b,"is:",math.pow(a,b))
        r = input("Do you want to continue with another operation?")
        if r == "n" or r == "no" or r == "NO" or r == "No":
            break
    else:
        break
