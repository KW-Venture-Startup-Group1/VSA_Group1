def solution(n, wires):
    answer = -1
    temp = []
    temp2 = []
    temp3 = []
    
    for i in range(n):
        temp.append([])

#    각 노드에 연결된 값을 저장합니다.
    for key in wires:
        [temp[key[0] - 1].append(key[1])]
        [temp[key[1] - 1].append(key[0])]

#     재귀함수를 통하여 특정 연결을 끊는 경우
#     한 노드에 몇개의 전력망이 연결되어 있는지를 계산합니다.
    for j in wires:
        temp2.append(branch(temp, j[0], j[1]))

#     가장 절반에 가깝게 분할된 경우를 찾습니다.
    for i in range(len(temp2)):
        val = n / 2 - temp2[i] 
        temp3.append(val if val > 0 else -val)
        
#     최종적으로 분할된 두 전력망의 길이의 차를 구합니다.
    answer = n - temp2[temp3.index(min(temp3))] * 2
    
    return answer if answer > 0 else -answer

#     특정 연결 ex) (1, 2)와 리스트를 입력받아
#     앞에 있는 노드에 얼마나 많은 전력망이 있는지 계산합니다.
def branch(tree, n, k):
    answer = 1
#     전역망이 하나만 연결되어 있는 경우입니다.
    if len(tree[n-1]) == 1:
        return answer
    
    temp = []
    temp.extend(tree[n - 1])
    temp.remove(k)
    
#     전력망이 여러개가 연결되어 있는 경우
#     자기 자신을 제외한 나머지 전력망을 종합합니다.
    for i in temp:
        answer += branch(tree, i, n)
    
    return answer