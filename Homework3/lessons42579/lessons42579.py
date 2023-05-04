def solution(genres, plays):
    answer = []
    #노래 Dictionary 생성
    songs = {g:[] for g in genres}
    #장르, 재생횟수, 인덱스를 묶음
    for z in zip(genres, plays, range(len(plays))):
        songs[z[0]].append([z[1] , z[2]])
    genre_sorted =sorted(list(songs.keys()), key= lambda x:sum(map(lambda y: y[0],songs[x])), reverse = True)
    for g in genre_sorted:
        i = [i[1] for i in sorted(songs[g],key= lambda x:(x[0],-x[1]), reverse = True)]
        answer += i[:min(len(i),2)]
    return answer
