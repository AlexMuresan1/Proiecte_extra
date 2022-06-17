import random

numberOfSreaks=0
for exps in range(10000):
    #creates a list of 100 "heads" and "tails" values
    list=[]
    for i in range(100):
        #0 is Head
        #1 is Tail
        x=random.randint(0,1)
        if x==0:
            list.append("H")
        else:
            list.append("T")

    #check if is a streak of 6 "heads" or 6 "tails"
    strks=1
    for i in range(len(list)):
        if i<=94:
            if list[i]=="H":
                if list[i+1]=="H":
                    if list[i+2]=="H":
                        if list[i + 3] == "H":
                            if list[i + 4] == "H":
                                if list[i + 5] == "H":
                                     numberOfSreaks+=1
                                     break
            elif list[i]=="T":
                if list[i+1]=="T":
                    if list[i+2]=="T":
                        if list[i + 3] == "T":
                            if list[i + 4] == "T":
                                if list[i + 5] == "T":
                                    numberOfSreaks+=1
                                    break
print("Chances of streak:",numberOfSreaks/100,"%")
