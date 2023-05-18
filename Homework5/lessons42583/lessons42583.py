
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_weight = 0
#     트럭의 무개로 queue를, 다리위의 트럭을 위한 빈 queue를 만듭니다.
    truck = deque(truck_weights)
    onbridge = deque([])
    
#     초기값 설정을 위해 하나를 뽑고 시작합니다.
    temp = truck.popleft()
    while True:
#         다리의 최대 무게보다 다음 트럭따지의 무게의 합이 적다면
        if bridge_weight + temp <= weight:    
#         트럭을 다리에 추가해주고 무게를 더합니다.
            onbridge.append(temp)
            bridge_weight += temp
#         트럭이 남아있을 경우 다음 실행을 위해 값을 추출합니다.
            if truck:
                temp = truck.popleft()
#         잔존 트럭이 없는 경우 종료합니다.
            else:
                break
#         무게를 초과할 경우 0을 추가해 줍니다.
#         (배열 길이 유지를 위함.)
        else:
            onbridge.append(0)
            
#         다리를 다 지났다면
        if bridge_length - 1 < len(onbridge):
#         가장 처음 들어간 트럭의 무게를 queue에서 제거하고 무게를 줄입니다.
            bridge_weight -= onbridge.popleft()
        
        answer += 1
    
#     마지막 트럭이 다리에 올라온 상태로 정료하였음으로 
#     현재까지의 길이 + 다리의 길이 + 마지막 트럭이 올라온 1을 더합니다.
    return answer + bridge_length + 1