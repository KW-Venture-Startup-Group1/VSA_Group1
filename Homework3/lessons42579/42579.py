#베스트앨범: https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    #노래 딕셔너리 생성
    songs = {g:[] for g in genres}
    #장르, 재생횟수, 인덱스를 묶음
    for z in zip(genres, plays, range(len(plays))):
        songs[z[0]].append([z[1] , z[2]])
        
    # 노래 재생 시간을 합산한 값이 높은 장르부터 낮은 장르까지 순서대로 정렬
    # map: 리스트의 요소를 지정된 함수로 처리해주는 함수
    # songs[x] 에서 x 는 노래 고유 번호임
    # map(lambda y: y[0],songs[x]) : songs[x] 딕셔너리를 리스트로 변환하고, y[0] 즉, 해당리스트의 첫 번째 값을 추출(첫 번째 값은 노래 재생 횟수를 의미)
    # sum으로 각 장르별 노래 재생 횟수가 제일 높은(reverse=True) 장르부터 정렬
    genre_sorted =sorted(list(songs.keys()), key= lambda x:sum(map(lambda y: y[0],songs[x])), reverse = True)
    
    # sorted(songs[g], key= lambda x:(x[0],-x[1]), reverse = True): songs[x] 딕셔너리 값을 리스트로 변환하고, 노래 재생 횟수를 기준으로 정렬
    # -x[1]: 재생 횟수를 내림차순으로 정렬하도록 하기 위해 추가
    for g in genre_sorted:
        i = [i[1] for i in sorted(songs[g], key= lambda x:(x[0],-x[1]), reverse = True)]
        # 각 장르별로 최대 2개까지(min) 출력
        answer += i[:min(len(i),2)]
    return answer


# 더 배울 수 있는 것들
# enumerate() 함수
# enumerate(): 인덱스(index)와 원소(element)에 동시 접근하면서 루프를 돌릴 수 있게 해줌
# enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 튜플(tuple)을 만들어줌
# (예)
#   for index, letter in enumerate(['A', 'B', 'C'])
#       print(index, letter)
# (실행결과)
#   0 A
#   1 B
#   2 C
