# H-In: https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    # n 편의 논문 중에서, h 번 이상 인용된 논문이 h 편이상이고
    # 나머지 논문이 h 번 이하 인용되었을 때, h 의 최댓값
    
    citations.sort(reverse=True)
    for num in range(0,len(citations)-1):
        if citations[0]==0:
            return 0
        if len(citations)==1:
            return 1 
        if citations[num]>=num+1 and citations[num+1]<=num+1:
            return num+1
    return len(citations)
