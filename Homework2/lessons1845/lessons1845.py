def solution(nums):
    arr=[]
    for i in nums:
        if i not in arr:
            arr.append(i)
    return len(nums)/2 if len(nums)/2 < len(arr) else len(arr)

