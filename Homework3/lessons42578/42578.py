# 의상: https://school.programmers.co.kr/learn/courses/30/lessons/42578

from collections import Counter
def solution(clothes):
    answer = 1
    Comb = Counter([clothes[i][1] for i in range(len(clothes))]).values()
    for j in Comb:
        answer *= (j+1)
    return answer-1
