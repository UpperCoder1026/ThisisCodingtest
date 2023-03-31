

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
    global step
    visit[r][c] = True #재귀하면 바로 Visit
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < n and nr >=0 and nc < n and nc >=0 :
            if L <= abs(data[nr][nc] - data[r][c]) <= R and visit[nr][nc] == False: 
                if not stack:
                    stack.append([r,c])
                stack.append([nr,nc])
                step += 1 # dfs_num 선언하고 더해주지 않으면 마지막에 stack을 리턴할 때 지도를 전부 안돌고 리턴해버린다
                dfs(nr,nc)
                step -= 1 
                continue                 
            else: pass
    if stack and step == 0: #step이 0이라는 것은 깊이 탐색을 한번만 한게아니라 여러 갈래로 한 것을 의미
        return stack
    else : return



def move(comm): # stack = [[1,2][2,3][3,2]]
    for i in range(len(comm)):
        sum = 0
        for j in range(len(comm[i])):
            r,c = comm[i][j] 
            sum += data[r][c]
        human = sum / len(comm[i])
        for j in range(len(comm[i])):
            r,c = comm[i][j] 
            data[r][c] = int(human)
    return #들여쓰기를 for문 안쪽으로 해서 한개하고 계속 나가졌다....return 잘하자...   



union = []

while True:
    for i in range(n):
        for j in range(n):
            if visit[i][j] == False:
                step = 0
                temp = dfs(i,j)
                if temp:
                    union.append(temp)
                    stack = []
                    temp = []
    if union:
        move(union)
        count += 1 # 한번이라도 인구이동이 있으면 count += 1
        visit = [[False]*n for _ in range(n)] #또 다시 새롭게 판을 짜야하기 때문에 visit을 새로 짬
        union = []  
    else : # 한번도 인구이동이 없으면 반복문 탈출
        break

print(count)
