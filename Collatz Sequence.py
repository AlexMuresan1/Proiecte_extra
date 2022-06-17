
def collatz(number):
     if number%2==0:
        return number//2
     else:
        return 3*number+1


try:
    n=int(input("Enter number:"))
    x=collatz(n)
    print(x)
    while x!=1:
        x=collatz(x)
        print(x)
except ValueError:
    print("ERROR! Enter an integer value!")
