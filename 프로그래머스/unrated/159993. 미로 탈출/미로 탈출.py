from collections import deque
def solution(maps):
    answer = 0
    for idx, idata in enumerate(maps):
        for jdx, jdata in enumerate(idata):
            if jdata == 'S':
                start = (idx,jdx)
            if jdata == 'E':
                end = (idx,jdx)
            if jdata == 'L':
                lever = (idx,jdx)
    def BFS(x,y,kx,ky):
        q = deque()
        q.append((x,y,0))
        visit = [[True for _ in range(len(maps[0]))] for _ in range(len(maps))]
        nx= [1,-1,0,0]
        ny =[0,0,1,-1]
        while q:
            x,y,cnt = q.popleft()
            if x == kx and y == ky:
                return cnt
            for i in range(4):
                dx = x + nx[i]
                dy = y + ny[i]
                if 0 <= dx < len(maps) and 0 <= dy < len(maps[0]) and visit[dx][dy] and maps[dx][dy] != 'X':
                    visit[dx][dy] = False
                    q.append((dx,dy,cnt+1))
        return -1
    a = BFS(start[0],start[1],lever[0],lever[1])
    if a != -1:
        answer += a
    else:
        return -1
    a = BFS(lever[0],lever[1],end[0],end[1])
    if a!= -1:
        answer += a
    else:
        return -1
    return answer
