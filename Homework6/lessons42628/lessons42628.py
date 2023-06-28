from heapq import *

def solution(operations):
    heap = []
    
#     작업을  기준으로 루프를 진행합니다.
    for set in operations:
#         입력이 I인 경우 뒤 숫자를 Int형식으로 변환한 뒤 추가합니다.
        if "I" in set:
            heap.append(int(set[2:]))
        
#         입력 연산이 D -1인 경우 min Heap을 이용하여
#         최솟값을 추출해 냅니다.
        elif set == "D -1" and heap:
            heapify(heap)
            heappop(heap)
            
#         입력 연산이 D 1인 경우 Max Heap을 이용하여
#         최댓값을 추출해 냅니다.
        elif set == "D 1" and heap:
            temp = []
            
#             Max Heap을 이용하기 위해 본인과 부호만 다른 인자를
#             추가하여 역순 정렬이 되도록 설정해 줍니다.
            for set in heap:
                heappush(temp, [-set, set])
            heappop(temp)
            heap = []
#             추출된 최댓값을 제외한 값들을 다시 복원합니다.
            for set in temp:
                heap.append(set[1])
        else:
            continue

#     Heap이 비어있는 경우 출력합니다.
    if not heap:
        return [0, 0]
#     Heap이 들어있는경우 출력합니다.
    else:
        return [max(heap), min(heap)]
    return 