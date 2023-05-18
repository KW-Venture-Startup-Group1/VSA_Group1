from collections import deque

def solution(price):
#     가격을 queue에 입력합니다.
    queue = deque(price)
    answer = []
    
#     현재 진행값 set, 기간 count를 설정합니다.
    set, count = 0, 0
    while True:
#         모든 가격들을 다 돌았다면 break 합니다.
        if set == len(price):
            return answer
    
        temp = queue.popleft()
        
#         현 위치부터 가격대의 끝까지 진행합니다.
        for i in range(set, len(price)):
#         가격이 떨어지거나 마지막이라면
            if temp > price[i] or i == len(price) - 1:
#         기간을 저장하고 break합니다.
                answer.append(count)
                break
#         아닌 경우 기간을 +1 합니다.
            else:
                count += 1
            
        count = 0
        set += 1
        