def buildPalindrome(st):
    st2 = st
    j=''
    while st2!=st2[::-1]:
        j = j + st2[0]
        st2=st2[1:]    
    return st+j[::-1]