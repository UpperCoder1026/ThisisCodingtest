n,m = map(int,input().split())
state = list(map(int,input().split()))

mapp = []

for a in range(n):
    mapp.append(list(map(int, input().split())))

x = state[0]
y = state[1]
view = state[2]
nx = 0
ny = 0 
past=[[x,y]]
tries = 0

step = [[-1,0],[0,1],[1,0],[0,-1]]#북, 동, 남, 서

def turn_left():
    global view
    view -= 1
    if view == -1:
        view = 3

while True:
    turn_left()
    nx = x + step[view][0]
    ny = y + step[view][1]
    tries += 1
    if mapp[nx][ny] == 0 and [nx,ny] not in past:
        past.append([nx,ny])
        x = nx
        y = ny
        tries = 0
        continue    
    if tries == 4:
        nx = x - step[view][0]
        ny = y - step[view][1]
        if mapp[nx][ny] == 0:
            if [nx,ny] not in past:
                past.append([nx,ny])
            x = nx
            y = ny           
            break
print(len(past))

