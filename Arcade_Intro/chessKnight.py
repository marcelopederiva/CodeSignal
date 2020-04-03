def chessKnight(cell):
    alf = 'abcdefgh'
    alf = list(map(str,str(alf)))
    compare = [1,2,3,4,5,6,7,8]
    c=0
    cell = list(map(str,str(cell)))
    cell[0] = compare[alf.index(cell[0])]
    cell[1] = int(cell[1])
    
    posx = [cell[0]+1,cell[0]+1,cell[0]-1,cell[0]-1,cell[0]+2,cell[0]+2,cell[0]-2,cell[0]-2]
    posy = [cell[1]+2,cell[1]-2,cell[1]+2,cell[1]-2,cell[1]+1,cell[1]-1,cell[1]+1,cell[1]-1]
    
    print(posx,posy)

    for i in range(len(posx)):
        if posx[i]>0 and posx[i]<9:
            if posy[i]>0 and posy[i]<9:
                c+=1
    

    return c