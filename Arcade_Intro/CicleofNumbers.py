def circleOfNumbers(n, firstNumber):
    c =  firstNumber+n/2
    if c >=n:
        return c%n
    else:
        return c