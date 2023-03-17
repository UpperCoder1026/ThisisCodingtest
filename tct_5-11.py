
from collections import deque 



n,m = map(int,input().split())

maze = []

dr = [-1,1,0,0]
dc = [0,0,-1,1]

for _ in range(n):
    maze.append(list(map(int,input())))

def bfs(r,c):
    queue = deque()
    queue.append([r,c])
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            if maze[nr][nc] == 0:
                continue
            if maze[nr][nc] == 1:
                queue.append([nr,nc])
                maze[nr][nc] = maze[r][c] + 1
    return maze[n-1][m-1]

print(bfs(0,0))