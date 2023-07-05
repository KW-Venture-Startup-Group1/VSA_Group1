def solution(citations):
    answer = 0
    citations.sort()
    
#     전체 길이를 정의합니다.
    all = len(citations)
    
#     1부터 H-index가 가능한지 역순으로 검산해 봅니다.
    for i in range(1, all + 1):
#         정렬된 배열중 뒤에서 i번째의 논문이
#         i이상 인용되었다면 통과시킵니다.
        if citations[-i] >= i:
            answer = i
    
    return answer