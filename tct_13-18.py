






def right(List):
    stack = []
    for i in List:
        if stack and stack[-1] == "(" and i == ")":
            stack.append("(")
            if stack[-1] == stack[-2] == "(":
                stack.pop()
                stack.pop()
            else :
                pass
        else :
            stack.append(i)
    if not stack:
        return True
    return False 
    
def bal(List):
    l = 0
    r = 0
    for idx, value in enumerate(List):
        if value == ")":
            r += 1
            if r == l:
                return idx
        elif value =="(":
            l += 1
            if r ==l:
                return idx
    return 
                



def solution(p):
    answer = ""
    if right(p):
        return p
    fin_idx = bal(p)
    u =p[:fin_idx+1]
    u = list(u)
    v =p[fin_idx+1:]
    v = list(v)
    if right(u):
        for i in solution(v):
            u.append(i)
        for i in u:
            answer += i
        return answer
    elif not right(u):
        s = []
        s.append("(")
        for j in solution(v):
            s.append(j)
        s.append(")")
        u = u[1:-1]
        for ind,k in enumerate(u):
            if k == "(":
                u[ind] = ")"
            elif k == ")":
                u[ind] = "("
        for t in u:
            s.append(t)
        for i in s:
            answer += i 
    return answer

print(solution(")))((())(("))








