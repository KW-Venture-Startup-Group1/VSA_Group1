# 프로세스 : https://school.programmers.co.kr/learn/courses/30/lessons/42587#

# Case 1. Rotate 기능 이용
from collections import deque

def solution(priorities, location):
    deq, index_deq = deque(), deque()
    deq.extend(priorities)
    index_deq.extend(list(range(len(deq))))
    process_list=[]
    
    while deq:
        while len(deq) > 1 and deq[0] != max(deq):
            deq.rotate(-1)
            index_deq.rotate(-1)  
        deq.popleft()
        process_list.append(index_deq.popleft())
        
    process = list(enumerate(process_list))
    process.sort(key=lambda x:x[1])
    
    return process[location][0]+1
  
# Case 2. 크기 비교를 통한 해결
from collections import deque

def solution(priorities, location):
    process_list=deque()
    process_list.extend(enumerate(priorities))
    current_index=0

    while process_list:
        current = process_list.popleft()
        if any(current[1] < process[1] for process in process_list):
            process_list.append(current)
        else:
            current_index += 1
            if current[0] == location:
                return current_index
