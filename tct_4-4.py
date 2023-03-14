n,m = map(int,input().split())
state = list(map(int,input().split()))

mapp = []

for a in range(n):
    temper = list(map(int, input().split()))
    mapp.append(temper)

x = state[0]
y = state[1]
view = state[2]
nx = 0
ny = 0 
past=[[x,y]]
tries = 0

step = [[-1,0],[1,0],[0,1],[0,-1]]#북, 남, 동, 서
while True:
    if view == 1: #동쪽을 보고 있을 때
        view = 0
        nx = x + step[0][0]
        ny = y + step[0][1]
        tries += 1
        if mapp[nx][ny] == 0 and [nx,ny] not in past:
            past.append([nx,ny])
            x = nx
            y = ny
            tries = 0
            continue
    elif view == 2: #남쪽을 보고 있을 때
        view = 1
        nx = x + step[2][0]
        ny = y + step[2][1]
        tries += 1
        if mapp[nx][ny] == 0 and [nx,ny] not in past:
            past.append([nx,ny])
            x = nx
            y = ny
            tries = 0
            continue    
    elif view == 3: #서쪽을 보고 있을 때
        view = 2
        nx = x + step[1][0]
        ny = y + step[1][1]
        tries += 1
        if mapp[nx][ny] == 0 and [nx,ny] not in past:
            past.append([nx,ny])
            x = nx
            y = ny
            tries = 0
            continue
    elif view == 0: #북쪽을 보고 있을 때
        view = 3
        nx = x + step[3][0]
        ny = y + step[3][1]
        tries += 1
        if mapp[nx][ny] == 0 and [nx,ny] not in past:
            past.append([nx,ny])
            x = nx
            y = ny
            tries = 0
            continue
    if tries == 4:
        break
print(len(past))

