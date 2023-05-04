def solution(phone_book):
    phone = sorted(phone_book)
    print(phone)
    for str1, str2 in zip(phone, phone[1:]):
        #str2가 str1으로 시작되면 True 아니면 False
        if str2.startswith(str1):
            return False
    return True
