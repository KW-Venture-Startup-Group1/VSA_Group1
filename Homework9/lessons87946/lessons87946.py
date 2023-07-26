from itertools import permutations as pm

def solution(k, dungeons):
    answer = []
    length = len(dungeons)
    temp = []
    temp2 = []
    
#     던전의 개수만큼 숫자를 등록합니다.
    for i in range(length):
        temp.append(i)
        
#     던전 입장 순서 순열을 생성합니다.
    for i in pm(temp, length):
        temp2.append(i)
    
#     생성된 순열을 기준으로
#     입장 가능한 던전의 수를 계산합니다.
    for key in temp2:
        kr = k
        temp_ans = 0
        for set in key:
            if dungeons[set][0] > kr:
                continue
            else:
                kr -= dungeons[set][1]
                temp_ans += 1
        answer.append(temp_ans)
    
#     최대로 입장 가능한 던전의 수를 출력합니다.
    return max(answer)