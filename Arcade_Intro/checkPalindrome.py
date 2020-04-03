def checkPalindrome(inputString):
    if list(inputString) == list(inputString)[::-1]:
        return True
    else:
        return False
    
