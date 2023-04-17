def solution(participant, completion):
    participant.sort()
    completion.sort()
    par=participant
    com=completion
    answer=''
    if par[0:len(com)]==com[0:len(com)]:
        answer=par[len(com)]
    else:
        for i in range(0,len(com)):
            if par[i]!=com[i]:
                answer=par[i]
                break
    return answer

