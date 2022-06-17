import random,time,copy

WIDTH=20
HEIGHT=10

nextCells=[]
for x in range(WIDTH):
    column=[]
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append("#")
        else:
            column.append(" ")
    nextCells.append(column)

while True:
    print("\n\n\n\n\n")
    currentCells=copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end="")
        print()
    break