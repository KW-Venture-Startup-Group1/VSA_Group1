def solution(sizes):
    answer = 0
    temp_w = []
    temp_h = []
    
#     가로와 세로중 큰 값을 width에 작은 값을 height에 저장합니다.
    for set in sizes:
        temp_w.append(max(set))
        temp_h.append(min(set))
        
#     가로와 세로의 가장 큰 값들을 곱하여 답을 구합니다.
    answer = max(temp_w) * max(temp_h)
    
    return answer