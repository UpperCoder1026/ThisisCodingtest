

n , L , R = map(int,input().split())

data = []
visit = [] # visit은 필요하다.

for _ in range(n):
    data.append(list(map(int,input().split())))
    visit.append([False]*n)


count = 0 #인구 이동 횟수

dr = [-1,1,0,0]
dc = [0,0,1,-1]
 
stack = [] #한번 DFS를 돌렸을때 연합한 나라 정보

def dfs(r,c):#현재 지도에서 한개의 연합을 찾아내는 함수
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
                dfs_num += 1 # dfs_num 선언하고 더해주지 않으면 마지막에 stack을 리턴할 때 지도를 전부 안돌고 리턴해버린다
                dfs(nr,nc)
                dfs_num -= 1 
                continue                 
            else: pass
    if stack and dfs_num == 1: # stack에 아무것도 없을때 [r,c]를 추가했디때문에 dfs_numdms 1로 남는다.
        return stack
    else : return



def move(stack): # stack = [[1,2][2,3][3,2]]
    sum = 0
    for j in range(len(stack)):
        r,c = stack[j] 
        sum += data[r][c]
    human = sum / len(stack)
    for j in range(len(stack)):
        r,c = stack[j] 
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
                    move(temp)
                    flag = True
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
