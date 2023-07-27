# 완전탐색 : 모음사전 (https://school.programmers.co.kr/learn/courses/30/lessons/84512)

def solution(word):
    answer = len(word)
    coefficient = [781, 156, 31, 6, 1]
    order = 'AEIOU'
    
    for i in range(len(word)):
        answer+=order.find(word[i])*coefficient[i]
    
    return answer
