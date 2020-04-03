def adjacentElementsProduct(inputArray):
    var = -1000
    for i in range(0,len(inputArray)-1):       
        som = inputArray[i]*inputArray[i+1]
        if som > var:
            var = som
    return var            