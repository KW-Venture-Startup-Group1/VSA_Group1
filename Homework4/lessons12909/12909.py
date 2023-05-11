# 올바른 괄호 : https://school.programmers.co.kr/learn/courses/30/lessons/12909

#'('으로 시작하고, ')'으로 끝날 것
#'('와 ')'의 개수가 같을 것
# Case 1. list
def solution(s):
    num = 0
    for e in s:
        if e=='(':
            num+=1
        else:
            num-=1
        if num<0:
            return False
    return num==0
  
# Case 2. stack
def solution(s):
    stack = []
    for element in s:
        if element == '(':
            stack.append(element)
        elif stack and stack[-1] == '(':
            stack.pop()
        else:
            return False
    return len(stack) == 0 # 스택에 남아있는 값이 없으면 True
