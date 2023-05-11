# 같은 숫자는 싫어: https://school.programmers.co.kr/learn/courses/30/lessons/12906

# Case 1. using list
def solution(arr):
    answer=[]
    answer.append(arr[0])
    for i in range(len(arr)-1):
        if answer[-1]!=arr[i+1]:
            answer.append(arr[i+1])
    return answer
  
# Case 2. using deque
from collections import deque  # deque 모듈 import
def solution(arr):
    queue = deque([arr[0]])  # arr의 첫 번째 원소로 deque를 생성
    for i in range(1, len(arr)):
        # deque의 마지막 원소와 arr의 i번째 원소가 다르면 deque에 추가
        if queue[-1] != arr[i]:  
            queue.append(arr[i])
    return list(queue)  # deque를 list로 변환하여 반환
