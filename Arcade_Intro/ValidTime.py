def validTime(time):
    time = list(time.split(':'))
    time = list(map(int,time))
    if time[0]<24 and time[0]>=0:
        if time[1]<60 and time[1]>=0:
            
            return True
    return False