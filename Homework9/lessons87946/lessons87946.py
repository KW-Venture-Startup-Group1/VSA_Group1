# 완전탐색 : 피로도 (https://school.programmers.co.kr/learn/courses/30/lessons/87946)

from collections import deque

def solution(k, dungeons):
    answer = -1
    root = deque()
    root.append((k, []))
    while root:
        k, current = root.popleft()
        for i in range(len(dungeons)):
                a, b = dungeons[i]
                if (k>=a) and (i not in current):
                    tmp = current + [i]
                    root.append(((k-b), tmp))
                else:
                    answer = max(answer, len(current))
    return answer
