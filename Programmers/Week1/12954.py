def solution(x, n):
    #list(range(x,x*(n+1),x))
    return [x*(i+1) for i in range(0,n)]
