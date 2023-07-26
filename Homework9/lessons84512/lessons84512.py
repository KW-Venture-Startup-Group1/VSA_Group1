from itertools import permutations as pm

def solution(word):
    answer = 0
    words = []
    
#     중복을 허용하는 문자 집합을 생성하고 순열로 조합합니다.
    for i in range(1, 6):
        for key in pm("AAAAAEEEEEIIIIIOOOOOUUUUU", i):
            words.append(''.join(key))
    words = list(set(words))
    
#     순열을 정렬한 뒤 원하는 단어의 index를 찾습니다.
    words.sort()
    answer = words.index(word) + 1
    
    return answer