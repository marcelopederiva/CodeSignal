import string
def longestWord(text):
    low = list(string.ascii_lowercase)
    up = list(string.ascii_uppercase)
    s =[]
    
    for x in text:
        if x not in low and x !=' ': 
            if x not in up:
                text = text.replace(x,' ')
    print(text)
    text= text.split()
    for x in text:
        s.append(len(x))
    
    return text[s.index(max(s))]
