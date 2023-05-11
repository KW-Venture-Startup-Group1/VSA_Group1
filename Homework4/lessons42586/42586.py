# 기능개발 : https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    day = 0 # 배포일
    already = 0 # 이미 배포가 완료된 기능의 개수
    while already < n:
        if progresses[already] + day*speeds[already] >= 100:
            con = 0 # 배포일에 배포되는 기능의 개수
            while already < n and progresses[already] + day*speeds[already] >= 100:
                con += 1
                already += 1
            answer.append(con)
        day += 1
    return answer
