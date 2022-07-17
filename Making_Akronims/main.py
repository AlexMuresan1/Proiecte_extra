text=input("Please insert your text: ")

acr=""

for i in text:
    if i.isupper():
        acr+=i

if acr=="":
    print("There are no capital letters.")
else:
    print(acr)

