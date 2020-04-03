def electionsWinners(votes, k):
    c=0
    if k==0:
        if votes.count(max(votes))>1:
            return c
        else:
            c=1
            return c 
    votes.sort(reverse = True)
    c=1
    for i in range(len(votes)-1):
        if votes[i+1]+k > votes[0]:
            c +=1
    return c