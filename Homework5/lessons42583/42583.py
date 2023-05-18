# 다리를 지나는 트럭: https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque(0 for _ in range(bridge_length))  # 다리를 나타내는 deque
    total_weight = 0  # 다리 위의 트럭 무게의 합
    truck_weights = deque(truck_weights)  # 대기 중인 트럭

    while truck_weights:
        time += 1
        total_weight -= bridge.popleft()  # 다리에서 나가는 트럭의 무게를 빼줌

        if total_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            total_weight += truck
        else:
            bridge.append(0)  

    time += bridge_length  # 마지막 트럭이 다리를 건너는 시간

    return time
