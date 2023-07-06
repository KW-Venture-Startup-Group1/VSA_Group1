def solution(array, commands):
    return [sorted(array[com[0]-1: com[1]])[com[2]-1] for com in commands]
"""
def solution(array, commands):
    answer = []
    for com in commands:
        # 자르고 오름차순 정렬
        sorted_array=sorted(array[com[0]-1: com[1]]) 
        print(sorted_array)
        answer.append(sorted_array[com[2]-1])
    return answer
"""
