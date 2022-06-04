print("Welcome to ATM!")
sold=5789
chances=3
while chances>0:
    pin=input("Introduceti PIN-ul:")
    if pin=="1735":
        print("Ati introdus PIN-ul corect!")
        print("Apasati 1 pentru a depune bani.")
        print("Apasati 2 pentru a retrage bani.")
        print("Apasati 3 pentru interogare sold.")
        print("Apasati 4 pentru retragere card.")
        optiune=int(input("Alegeti o optiune:"))
        if optiune==1:
            print("Alegeti o suma de bani pentru a o depune: 10, 50, 100, 200, 300 sau alta suma")
            suma=int(input("Alegeti suma dorita:"))
            sold=sold+suma
            print("Soldul dumneavoastra dupa depunere este:",sold)
            r=input("do you want to continue?")
            if r =="No"or r=="no" or r=="n":
                print("Thank you!")
                break
        elif optiune==2:
            print("Alegeti o suma de bani pe care o doriti sa o retrageti din contul dvs: 10, 50, 100, 200, 300 sau alta suma")
            suma=int(input("Alegeti suma dorita:"))
            sold=sold-suma
            print("Soldul dumneavoastra dupa retragere este:",sold)
            r = input("do you want to continue?")
            if r =="No"or r=="no" or r=="n":
                print("Thank you!")
                break
        elif optiune==3:
            print("Soldul dvs este:",sold)
            r = input("do you want to continue?")
            if r =="No"or r=="no" or r=="n":
                print("Thank you!")
                break
        elif optiune==4:
            print("Asteptati retragerea cardului dvs!")
            print("Card retras!")
            r = input("do you want to continue?")
            if r =="No"or r=="no" or r=="n":
                print("Thank you!")
                break
    else:
        chances -= 1
        print("PIN-ul introdus este gresit!")
        print("Mai aveti",chances,"incercari!")
        if chances == 0:
            print("Ati epuizat incercarile de a introduce PIN-ul!")
            break
