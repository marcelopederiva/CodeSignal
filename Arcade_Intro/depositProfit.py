def depositProfit(deposit, rate, threshold):
    c = 1
    d = 0
    while d<1:
        
        deposit = deposit*(float(rate/100) +1)

        if deposit >= threshold:
            d = 1
            return c
        else:
            c+=1
        
