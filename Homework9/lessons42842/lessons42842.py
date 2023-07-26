def solution(brown, yellow):
    answer = []
    
#     노란색의 값이 나올수 있는 가로, 세로 길이를 조회합니다.
    for i in range(1, int(yellow ** 0.5 + 1)):
        if yellow % i:
            continue
            
#      위에서 조회한 값에서의 테두리의 크기가
#      갈색의 값과 같은지 비교합니다,
        if (2 * yellow // i + i * 2 + 4) == brown:
            answer.append(yellow // i + 2)
            answer.append(i + 2)
            break
    
    return answer