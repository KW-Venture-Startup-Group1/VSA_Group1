def solution(s):
    count = 0
    
#     문자열 s로부터 한글자씩 가져옵니다.
    for i in s:
#         첫 괄호는 반드시 '('여야 하며
#         '('와 ')'의 개수가 동일하면 다음은
#         반드시 '('가 와야 합니다.
        if i == '(' and count == 0:
            count += 1
        elif i == '(':
            count += 1
        elif i == ')' and count != 0:
            count -= 1
#         위 제약사항을 어기면 바로 False를 리턴합니다.
        else:
            return False
    
#     두 괄호의 수가 다르면 False를 리턴합니다.
    if count != 0:
        return False

    return True