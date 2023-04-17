def solution(s):
    p,y=s.count('p')+s.count('P'),s.count('y')+s.count('Y')
    return p==y
#p,Y의 개수가 같은 경우와 p,Y 모두 존재하지 않는 경우에 True를 리턴인데
#p,Y가 모두 존재하지 않는 경우 역시 p와 Y의 개수가 각각 0으로 같은 상황임

