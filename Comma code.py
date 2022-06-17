def comma(list):
    if len(list)==0:
        return False
    rez=""
    x=list[len(list)-1]
    y=len(list)-1
    for i in list:
        if i == x:
            rez+=i
        else:
            rez += i
            rez+=","
            rez+=" "
    p=0
    rez1=""
    rez2=""
    for i in range(len(rez)):
        if rez[i]==" ":
            p+=1
        if p==y:
            rez1=rez[0:i]
            rez2=rez[i+1:len(rez)]
            rez=rez1+" and "+rez2
            break
    return rez


spam=["salut","dada","cats"]
rez=comma(spam)
if rez!=False:
    print(rez)
else:
    print("List is null")