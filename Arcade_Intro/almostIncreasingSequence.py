def almostIncreasingSequence(sequence):

    counter = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            continue
        elif i == 1 or i == len(sequence) - 1:
            counter += 1
        elif sequence[i] > sequence[i-2]:
            counter += 1
        elif sequence[i+1] > sequence[i-1]:
            i += 1
            counter += 1
        else:
            return False
        
        if counter > 1:
            return False
    return True
    
    
    
    
