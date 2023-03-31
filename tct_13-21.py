

n , L , R = map(int,input().split())

data = []
visit = []

for _ in range(n):
    data.append(list(map(int,input().split())))
    visit.append([False]*n)


count = 0

dr = [-1,1,0,0]
dc = [0,0,1,-1]

stack = []
comm = []

def dfs(r,c):#여기서 연합들을 반환해줘야함
    global dfs_num
    visit[r][c] = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < n and nr >=0 and nc < n and nc >=0 :
            if abs(data[nr][nc] - data[r][c]) >= L and abs(data[nr][nc] - data[r][c]) <= R and visit[nr][nc] == False: 
                if not stack:
                    stack.append([r,c])
                    dfs_num += 1
                stack.append([nr,nc])
                dfs_num += 1
                dfs(nr,nc)
                dfs_num -= 1
                continue                 
            else: pass
    if stack and dfs_num == 1:
        return stack
    else : return



def move(stack): # stack = [[[1,2][2,3][3,2]][[4,1][4,2][4,3]][]]
    for i in range(len(stack)):
        sum = 0
        for j in range(len(stack[i])):
            if stack[i][j]:
                r,c = stack[i][j] 
                sum += data[r][c]
            else: pass
        human = sum / len(stack[i])
        for j in range(len(stack[i])):
            if stack[i][j]:
                r,c = stack[i][j]
                data[r][c] = int(human)
    return   
flag = False

while True:
    for i in range(n):
        for j in range(n):
            if visit[i][j] == False:
                dfs_num = 0
                temp = dfs(i,j)
                if temp:
                    comm.append(dfs(i,j))    
                    move(comm)
                    flag = True
                    comm =[]
                    stack = []
                    temp = []
                else : pass
            if i == n-1 and j == n-1:
                break
        if i == n-1 and j == n-1:
            break    
    if not flag:
        break
    count += 1 
    visit = [[False]*n for _ in range(n)]
    flag = False
    

print(count)
