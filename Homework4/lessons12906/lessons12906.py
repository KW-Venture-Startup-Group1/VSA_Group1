def solution(arr):
#     처음 값을 기준으로 삼기위해 넣어줍니다.
    answer = [arr[0]]
    
#     두번째 값부터 이전 값과 비교한 뒤
#     다르면 answer에 추가합니다.
    for i in range(1, len(arr)):
        if answer[len(answer) - 1] != arr[i]:
            answer.append(arr[i])
        else:
            continue
    
    return answer