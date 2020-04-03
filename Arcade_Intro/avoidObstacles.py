def avoidObstacles(inputArray):
    n = 2
    while 1:
        for i in inputArray:
            if i % n == 0: break
        else:
            break
        n += 1
    return n