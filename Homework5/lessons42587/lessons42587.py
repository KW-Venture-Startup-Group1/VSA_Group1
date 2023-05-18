from collections import deque

def solution(priorities, location):
#     우선순위를 queue에 넣어줍니다.
    queue = deque(priorities)
#     우선순위가 큰 순서대로 정렬 합니다.
    priorities.sort(reverse = True)
    
    set = 0
    while True:
#         가장 큰 우선순위부터 검사합니다
        i = priorities[set]
        temp = queue.popleft()
#         두 우선순위가 같은 경우
        if i == temp:
#         현재 우선순위가 현재 추출된 우선순위와 같은지 검사합니다.
            if location == (len(priorities) - len(queue) - 1):
                return location + 1
            else:
                set += 1
        else:
#             우선순의가 다른경우 다시 queue에 추가하고
            queue.append(temp)
#     우선순위의 현위치를 변경합니다.
            if location == set:
                location = len(priorities) - 1
            else:
                location -= 1
    