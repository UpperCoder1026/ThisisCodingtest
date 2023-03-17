



def dfs(frame,x,y,visited):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if frame[x][y] == 0 and visited[x][y] == False:
        visited[x][y] = True
        dfs(frame,x+1,y,visited)
        dfs(frame,x-1,y,visited)
        dfs(frame,x,y+1,visited)
        dfs(frame,x,y-1,visited)
        return True
    return False

n, m = map(int, input().split())

ice = 0
frame = []

for i in range(n):
    frame.append(list(map(int,input().split())))

visited = [] 

for i in range(n):
    visited.append([False for _ in range(len(frame[i]))])

for j in range(n):
    for h in range(m):
        if dfs(frame,j,h,visited) == True:
            ice += 1

print(ice)