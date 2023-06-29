# 더 맵게: https://school.programmers.co.kr/learn/courses/30/lessons/42626

# Case 1. 단순 List 정렬을 이용
def solution(scoville, K):
    count=0
    scoville.sort()
    while(scoville[0]<K):
        scoville.sort() # 내림차순 정렬
        
        first_min_scoville = scoville.pop(0)
        second_min_scoville = scoville.pop(0)
        
        mix_scoville = first_min_scoville + second_min_scoville * 2
        scoville.append(mix_scoville)
        count+=1
        
        if (len( scoville)==1 and  scoville[0]<K):
            return -1      
    return count

# Case 2. Heap 자료구조를 이용
import heapq
def solution(scoville, K):
    heap = scoville
    heapq.heapify(heap) # 시간 복잡도: O(logn)
    count=0
    while(heap[0]<K):
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap)*2)
        count+=1
        if (len(heap)==1 and heap[0]<K):
            return -1
    return count
