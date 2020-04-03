from math import floor
def centuryFromYear(year):
    p=1
    i = 0
    j = 100
    k=1
    while p!=0:

        if (year<j+1):
            sec = k
            p=0
        else:
            i = i+100
            j = j+100
            k = k+1   
            
    return sec
