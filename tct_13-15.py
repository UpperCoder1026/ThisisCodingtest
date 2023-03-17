






from collections import deque

n,m,k,x = map(int,input().split())
 
# road라는 빈 리스트를 생성, m+1 만큼의 row들을 미리 추가
road = [[] for _ in range(n+1)]  #숫자가 나오지 않는다면 이 방식으로 빈 리스트를 만드는 것이 매우 좋다.

for _ in range(m): #인접 리스트를 만드는 방식
    c1,c2 = list(map(int,input().split()))
    road[c1].append(c2)

visited = [False for _ in range(n+1)] #"[False] * n+1" 이런 구문은 안됨

def bfs(way_num,start):
    queue = deque()
    dist = 1 
    just_city = []
    queue.append([start,road[start][0],dist])
    visited[road[start][0]] = True
    if dist == way_num:
        just_city.append(road[start][0])
    # 첫번째 거리 탐색
    if len(road[start]) >= 2:
        for i in range(1,len(road[start])):
            queue.append([start,road[start][i],dist])
            visited[road[start][i]] = True
            if dist == way_num:
                just_city.append(road[start][i])
    # 두번째 거리부터]
    while queue:
        _,nstart,_ = queue.popleft()
        if not road[nstart]:
            continue
        if road[nstart]:
            for j in range(1,len(road[nstart])):
                if visited[road[nstart][j]] == False:
                    dist += 1
                    queue.append([start,road[nstart][j],dist])
                    visited[road[nstart][j]] = True
                    if dist == way_num:
                        just_city.append(road[nstart][j])
            if dist == way_num:
                break
    return just_city

city = bfs(k,x)
if not city:
    print(-1)
for l in range(len(city)):
    print(city[l])
        

    
