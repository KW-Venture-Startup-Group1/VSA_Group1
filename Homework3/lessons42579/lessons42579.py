def solution(genres, plays):
    dict = {}
    answer = []
    seq = []
    
#     딕셔너리 내부의 value값으로 새로운 딕셔너리를 넣어줍니다.
    for i in range(len(genres)):
        if not (dict.get(genres[i])):
            dict[genres[i]] = {i: plays[i]}
#             장르별 재생수를 종합합니다.
            dict[genres[i]].update({'count':plays[i]})
        else: 
            dict[genres[i]].update({i: plays[i]})
            dict[genres[i]]['count'] += plays[i]
    
#     장르별로 재생수를 2차원 배열로 뽑아와 
    for i in dict:
        seq.append([dict[i]['count'], i])
#     재생수가 많은 순서대로 정렬합니다.
    seq.sort(reverse = True)
    
#     정렬된 순서에 따라 접근합니다.
    for i in seq:
#         정렬에 방해가되는 count값을 제거해 줍니다.
        del dict[i[1]]['count']
#         재생수가 많은순/ 고유번호가 작은순으로 정렬합니다.
        s = sorted(dict[i[1]].items(), key = lambda x : (-x[1], x[0]))
        count = 0
#         최대 2회까지만 answer 배열에 추가합니다.
        for j in s:
            answer.append(j[0])
            count += 1
            if count == 2:
                break
    
    return answer