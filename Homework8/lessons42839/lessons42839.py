from itertools import permutations as pm

def solution(numbers):
    answer = 0
    length = len(numbers)
    num = []
    setting = False
    
#     모든 배열 가능한 방식을 순열을 이용하여 추출합니다.
    for i in range(1, length + 1):
        for j in pm(numbers, i):
            num.append(''.join(j))
            
#     숫자로 바꾼 뒤 중복 제거를 위하여 집합을 이용합니다.
    num = list(set(map(int, num)))
    
#     각 숫자가 소수인지를 판별합니다.
    for i in num:
        setting = True
        if i == 0 or i == 1:
            continue
        elif i == 2:
            answer += 1
            continue
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                setting = False
                break
                
        if setting:
            answer += 1
    
    return answer 