def solution(array, commands):
    answer = []
    
#     각 command 별로 시행합니다.
    for set in commands:
#         배열을 command의 기준에 맞게 인덱싱 한뒤
        temp = array[set[0] - 1: set[1]]
#         해당 배열을 정렬하여 원하는 값을 출력합니다.
        temp.sort()
        answer.append(temp[set[2] - 1])
    return answer