# 디스크 컨트롤러: https://school.programmers.co.kr/learn/courses/30/lessons/42627

from heapq import heapify, heappush, heappop

def solution(jobs):
    den = len(jobs)
    time_now = 0
    time_before = -1
    num = 0
    arr = []
    check = 0
    while check < len(jobs):
        for j in jobs:
            if time_before < j[0] <= time_now:
                heappush(arr, [j[1], j[0]])
        if arr:
            now = heappop(arr)
            time_before = time_now
            time_now += now[0]
            num += time_now-now[1]
            check += 1
        else: time_now += 1
    return int(num / den)
