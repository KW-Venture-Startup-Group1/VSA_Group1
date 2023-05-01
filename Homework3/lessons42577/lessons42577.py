def solution(phone_book):
    phone_book.sort()
    dict = {}

#     전화번호를 딕셔너리에 저장
    for i in range(len(phone_book)):
        dict[i] = phone_book[i]
        
#     정렬되었을 경우 11 112의 순으로 정렬되며 다음게 접두사가 아니라면
#     그 다음수 역시 접두사가 될 수 없음으로 
#     정렬된 딕셔너리를 차례대로 비교함
    for i in range(len(phone_book) - 1):
#         startswith <= 접두사인지 비교해주는 함수
        if (dict[i + 1].startswith(dict[i])):
            return False
        
    return True