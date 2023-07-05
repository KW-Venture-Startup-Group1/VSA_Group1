def solution(numbers):
    answer = ''
    setting = []
    zero = 0

#     입력된 숫자들을 자릿수로 분리합니다.
    for set in numbers:
        if set == 1000:
            setting.append([1000, 1, 0, 0, 0])
            zero += 1
        elif set >= 100:
            temp1 = set // 100 % 10
            temp2 = set // 10 % 10
            temp3 = set % 10
#             숫자가 자릿수에 맞게 반복되도록 작성해 줍니다.
            setting.append([set, temp1, temp2, temp3, temp1])
            zero += 1
        elif set >= 10:
            temp1 = set // 10 % 10
            temp2 = set % 10
            setting.append([set, temp1, temp2, temp1, temp2])
            zero += 1
        else:
            setting.append([set, set, set, set, set])
            zero = (zero + 1) if set != 0 else zero
        
#         각 자릿수를 기준으로 정렬해 줍니다.
    setting.sort(key= lambda x : (x[1], x[2], x[3], x[4], -x[0]))

#     문자열을 출력합니다.
    for ans in setting:
        answer = str(ans[0]) + answer
    
#     모든 내용물이 0인 경우를 예외처리 해 줍니다.
    return answer if zero else '0'