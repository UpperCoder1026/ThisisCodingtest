position = input()
row = int(position[1])
col = int(ord(position[0])-int(ord('a')))+1

nrown, ncol = 0 ,0
count = 0 

step = [[2,1],[2,-1], [-2,1], [-2,-1],[-1,2],[-1,-2],[1,2],[1,-2]]

for i in range(len(step)):

    nrow = row + step[i][0]
    ncol = col + step[i][1]
    if nrow > 8 or ncol >8 or nrow < 1 or ncol <1:
        continue
    count += 1

print(count)
