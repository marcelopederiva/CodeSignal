def commonCharacterCount(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    c= 0
    for i in range(0,len(s1)):
        print(i)
        for j in range(0,len(s2)):
            if i != len(s1) and s1[i]==s2[j]:
                print(s1[i])
                c +=1
                s2.remove(s2[j])
                break

    return c