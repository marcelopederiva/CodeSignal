def addBorder(picture):
    for i in range(0,len(picture)):
        copy = picture[i]
        picture[i] = '*'+copy+'*'       
    picture.insert(0,'*'*len(picture[0]))
    picture.insert(len(picture)+1,'*'*len(picture[1]))
    return picture