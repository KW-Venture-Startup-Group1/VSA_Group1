def solution(answers):
    answer = [0, 0, 0]
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    temp1, temp2, temp3 = len(a1), len(a2), len(a3)
    
#     정답을 각각 추출한 뒤 각 학생들이 찍은 답과 비교합니다.
    for i in range(len(answers)):
#         학생의 찍는 패턴을 저장한 뒤 이를 반복적으로 비교합니다.
        if answers[i] == a1[i % temp1]:
            answer[0] += 1
        if answers[i] == a2[i % temp2]:
            answer[1] += 1
        if answers[i] == a3[i % temp3]:
            answer[2] += 1
    
#     가장 많이 맞춘 숫자를 얻은 뒤 어느 학생인지를 판별하여 출력합니다.
    student = []
    temp = max(answer)
    for i in range(3):
        if answer[i] == temp:
            student.append(i + 1)
    
    return student