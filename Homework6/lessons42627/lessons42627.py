from heapq import *

def solution(jobs):
#     작업을 정렬해 줍니다.
    jobs.sort()
#     전체 진행 시간의 초깃값을 설정해 줍니다.
#     최초 진행 시간은 최초 작업 시작시간 + 최초 작업의 길이 입니다.
    count = jobs[0][0] + jobs[0][1]
#     전체 요청부터 종료까지의 시간을 설정해 줍니다.
    answer = jobs[0][1]
    reverse = []
    
#     Heap으로 변환하기 편하도록 요청시간과 작업시간을 바꾼 배열을 하나 생성합니다.
    for set in jobs[1:]:
        reverse.append([set[1],set[0]])
    
    temp = []
    heapify(reverse)
    
#     한 프로세스 종료 동안 요청된 작업들 중
#     가장 빨리 끝나는 작업이 먼저 실행되도록 구성하였습니다.
    while reverse:
        temp2 = heappop(reverse)
        
#         가장 작은 작업시간을 가지는 작업이
#         방금 진행한 작업 도중에 요청이 온 경우입니다.
        if temp2[1] <= count:
#         프로세스의 실행시간 만큼 전체 진행시간을 증가시킵니다.
            count += temp2[0]
            answer += (count - temp2[1])
#         예외처리를 위해 빼두었던 요청들을 다시 합칩니다.
            for setting in temp:
                heappush(reverse, setting)
            temp = []
#         작업 완료 후 요청까지의 거리가 있어
#         바로 실행할 수 없음으로 넘기게 됩니다.
        else:
            temp.append(temp2)
        
#         만일 모든 요청이 겹치지 않는 경우의 예외처리 입니다.
        if not reverse and temp:
#         임시 배열을 요청시간 순으로 정렬합니다.
            temp.sort(key = lambda x: [x[1], x[0]])
#         겹치는 것이 없음으로 요청시간과 처리 시간을 재 정의 해줍니다.
            count = temp[0][1] + temp[0][0]
            answer += (count - temp[0][1])
            for setting in temp[1:]:
                heappush(reverse, setting)
            temp = []
        
    return answer // len(jobs)