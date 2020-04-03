def firstDuplicate(a):
    t =set()
    for i in a:
        if i in t:
            return i
        t.add(i)
    return -1