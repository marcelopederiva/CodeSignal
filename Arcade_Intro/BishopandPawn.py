def bishopAndPawn(bishop, pawn):
    alf = 'abcdefgh'
    alf = list(map(str,str(alf)))
    compare = [1,2,3,4,5,6,7,8]
    ocp =[]
    bishop = list(map(str,str(bishop)))
    bishop[0] = compare[alf.index(bishop[0])]
    bishop[1] = int(bishop[1])
    
    pawn = list(map(str,str(pawn)))
    pawn[0] = compare[alf.index(pawn[0])]
    pawn[1] = int(pawn[1])
    
    if abs(bishop[0]-pawn[0])==abs(bishop[1]-pawn[1]):
        return True
    else:
        return False
    
    