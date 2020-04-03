def chessBoardCellColor(cell1, cell2):
    alf = 'ABCDEFGH'
    alf = list(map(str,str(alf)))
    compare = [1,2,3,4,5,6,7,8]
    
    cell1 = list(map(str,str(cell1)))
    cell1[0] = compare[alf.index(cell1[0])]
    cell1[1] = int(cell1[1])
    
    cell2 = list(map(str,str(cell2)))
    cell2[0] = compare[alf.index(cell2[0])]
    cell2[1] = int(cell2[1])
    
    if cell1[0]%2 == 0 and cell1[1]%2 == 0:
        if cell2[0]%2 == 0 and cell2[1]% 2== 0:
            return True
        elif cell2[0]%2 != 0 and cell2[1]% 2!= 0:
            return True
        else:
            return False
    if cell1[0]%2 != 0 and cell1[1]%2 != 0:
        if cell2[0]%2 != 0 and cell2[1]% 2!= 0:
            return True
        elif cell2[0]%2 == 0 and cell2[1]% 2== 0:
            return True
        else:
            return False
    if cell1[0]%2 != 0 and cell1[1]%2 == 0:
        if cell2[0]%2 == 0 and cell2[1]%2 == 0:
            return False
        elif cell2[0]%2 != 0 and cell2[1]%2 != 0:
            return False
        else:
            return True
        
    if cell1[0]%2 == 0 and cell1[1]% 2!= 0:
        if cell2[0]%2 == 0 and cell2[1]%2 == 0:
            return False
        else:
            return True    