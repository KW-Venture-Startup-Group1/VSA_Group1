def solution(progresses, speeds):
    answer = []
    complete = []
    
#     각 기능이 개발되는데 걸리는 시간을 계산합니다.
    for i in range(len(progresses)):
        temp = (100 - progresses[i]) // speeds[i] if (100 - progresses[i]) % speeds[i] == 0 else (100 - progresses[i]) // speeds[i] + 1
        complete.append(temp)
        
#     처음 배포되는 기능을 기준으로 잡습니다.
    set = complete[0]
    count = 0
    for i in complete:
        if i <= set:
            count += 1
        else:
            set = i
            answer.append(count)
            count = 1
            
#     마지막으로 배포되는 숫자를 추가합니다.
    answer.append(count)
        
    return answer