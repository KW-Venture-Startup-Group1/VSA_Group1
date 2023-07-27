완전탐색 : 카펫 (https://school.programmers.co.kr/learn/courses/30/lessons/42842)

# Code 1
import math
def solution(brown, yellow):
    #equation: x^2 - px + q = 0
    p = (brown-4)/2
    q = yellow
    D = math.sqrt(p**2 - 4*q) # math.sqrt(Discriminant)
    return [(p+D)/2 +2, (p-D)/2 +2

# Code 2
import math
def solution(brown, yellow):
    total = brown+yellow
    for colum in range(3,int(math.sqrt(total))+1):
        if total%colum == 0:
            row = total/colum
            if (colum-2)*(row-2) == yellow:
                       return [row, colum]
