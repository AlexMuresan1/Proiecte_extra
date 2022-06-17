def isValidChessBoard(dict):
    valid=1
    a=len(dict)
    if a>32:
        valid=0
    for i in dict:
        x=int(i[0])
        y=i[1]
        if x>8:
            valid=0
            break
        elif y>"i":
            valid=0
            break
    cb=0
    cw=0
    for i in dict:
        x=dict[i]
        if x=="bking":
            cb+=1
        elif x=="wking":
            cw+=1
    if cb>1 or cw>1:
        valid=0
    cp=0
    for i in dict:
        if dict[i]=="wpawn" or dict[i]=="bpawn":
            cp+=1
    if cp>8:
        valid=0
    return valid

dict={"1h":"bking","6c":"wqueen","2g":"bbishop","5h":"bqueen","3e":"wking","5b":"wrook"}
if isValidChessBoard(dict)==1:
    print("Valid board")
else:
    print("Invalid board")
