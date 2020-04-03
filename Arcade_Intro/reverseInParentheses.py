def reverseInParentheses(a):
    i=0
    while i < len(a):
        if (a[i]=='('):
            start=i
        if (a[i]==')'):
            end=i
            b=a[start:end+1]
            c=b[1:len(b)-1][::-1]
            a=a.replace(b,c)
            i=-1
        i+=1
    return a
    
