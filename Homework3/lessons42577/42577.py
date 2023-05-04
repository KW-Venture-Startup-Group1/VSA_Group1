# 전화번호 목록: https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone = sorted(phone_book)
    print(phone)
    for str1, str2 in zip(phone, phone[1:]):
        #str2가 str1으로 시작되면 True 아니면 False
        if str2.startswith(str1):
            return False
    return True

# 더 공부할 수 있는 내용들 - filter (https://www.daleseo.com/python-filter/)
# filter() 함수: filter(조건 함수, 순회 가능한 데이터)
# filter() 함수는 두번째 인자로 넘어온 데이터 중에서 첫번째 인자로 넘어온 조건 함수를 만족하는 데이터만을 반환
