def solution(clothes):
    answer = 1
    dict = {}
    
#     옷을 종류: 이름으로 딕셔너리에 저장
    for i in clothes:
#         새로 추가하는지 기존 종류에 추가할지 구분
        if not dict.get(i[1]):
            dict[i[1]] = [i[0]]
        else:
            dict[i[1]].append(i[0])
            
#     해당 부분을 안입는 경우를 포함한 모든 가지수를 구합니다
    for i in dict.values():
        answer *= (len(i) + 1)
    
#     전부 벗는 경우를 제외하고 출력합니다.
    return answer - 1