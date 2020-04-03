import string
def sumUpNumbers(a):
    num = list(string.digits)  
    for x in a:
        if x not in num and x !=' ': 
            a = a.replace(x,' ')
    a= a.split()
    print(a)
    n=[]
    for i in a:
        try:
            n.append(int(i))
        except:
            continue
    print(n)
    return sum(n)
