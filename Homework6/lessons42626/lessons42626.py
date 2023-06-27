from heapq import *;

def solution(scoville, K):
    answer = 0
    
#     주어진 스코빌 배열을 힙으로 변환합니다.
    heapify(scoville)
    
    while True:
#         힙에서 최솟값을 뽑아냅니다.
        temp = heappop(scoville)
    
#     최솟값이 스코빌 지수를 만족하면 횟수를 출력합니다.
        if temp >= K:
            return answer 
#     스코빌 지수를 만족시킬 수 없으면 -1을 출력합니다.
        elif len(scoville) == 0:
            return -1
        else:
#     스코빌 지수 만족을 위해 주어진 계산식대로 연산합니다.
            temp2 = temp + 2 * heappop(scoville)
            answer += 1
#     더 높아진 스코빌 지수를 힙에 넣습니다.    
            heappush(scoville, temp2)