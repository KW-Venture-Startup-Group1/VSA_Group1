# 주식가격 : https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    length = len(prices)
    answer = [0] * length  # 결과를 저장할 리스트

    for i in range(length - 1):
        for j in range(i + 1, length):
            answer[i] += 1  # 가격이 떨어지지 않았으므로 1초씩 더하기
            if prices[j] < prices[i]:  # 가격이 떨어졌을 경우 종료
                break
                
    return answer
