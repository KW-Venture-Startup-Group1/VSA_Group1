# 완전탐색 : 피로도 (https://school.programmers.co.kr/learn/courses/30/lessons/86971)

# Depth First Search 
def DFS(root, wires, child):
    global tmp
    
    for i in range(len(child)-1):
        if child[i]==0:
            for j in range(2):
                if wires[i][j] == root:
                    child[i]=1
                    tmp+=1
                    DFS(wires[i][(j+1)%2],wires,child)
                    child[i]=0
                    
def solution(n, wires):
    ch=[0]*n
    res=[]
    global tmp
    
    for i in range(n-1):
        tmp=1
        ch[i]=1
        x,y=wires[i][0],wires[i][1]
        
        DFS(x,wires,ch)
        ch[i]=0
        res.append(abs(2*tmp-n)) 
    return min(res)
