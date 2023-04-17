def solution(s):
    P = 0
    Y = 0
    
    for i in s.upper():
        if (i == "Y"):
            Y += 1
        elif (i == "P"):
            P += 1
    
    if(P == Y):
        return True
    else:
        return False