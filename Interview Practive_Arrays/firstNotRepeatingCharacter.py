def firstNotRepeatingCharacter(s):
    t = {}
    for i in s:
        if i not in t:
            t[i]=1
        else:
            t[i]+=1
    for i in t:
        if t[i]==1:
            return i
        else:
            continue
    return '_'
