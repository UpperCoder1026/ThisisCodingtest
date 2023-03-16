from collections import deque

n,k = map(int,input().split()) #시험관의 줄 수, 바이러스의 수

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split()))) #시험관 내 바이러스 분포

s,x,y = map(int,input().split())

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(s,x,y):
    # 큐 생성
    queue = deque()
    # 큐 내 바이러스 위치 탐색 & 인큐 (기본 셋팅) 
    for u in range(1,k+1):
        for i in range(n):  
            for j in range(3):
                if graph[i][j] == u:
                    queue.append([i,j,u])
    # 너비 우선 탐색 진행
    count = 0
    while queue :
        if count == s:
            break
        r,c,num = queue.popleft()
        if num == 1:
            count += 1
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if nr < 0 or nc <0 or nr >= n or nc >= 3:
                continue
            if graph[nr][nc] > 0:
                continue
            if graph[nr][nc] == 0:
                graph[nr][nc] = num
                queue.append([nr,nc,num])

    return graph[x-1][y-1]

print(bfs(s,x,y))