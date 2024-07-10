N,e,w,n,s = map(int,input().split())

all_cnt = 4 ** (N)

probabilities = [0.01 * e, 0.01 * w, 0.01 * n,0.01 * s]
smart_cnt = 0
visited = set()
visited.add((0,0))
moves = [
    [0,1],
    [0,-1],
    [1,0],
    [-1,0]
]
ans = 0
def DFS(x,y,depth,probability):
    global ans
    if probability == 0:
        return
    if depth == N:
        ans += probability
        return
    for idx,move in enumerate(moves):
        xx,yy = move
        dx = x + xx
        dy = y + yy
        if (dx,dy) in visited:
            continue
        visited.add((dx,dy))
        DFS(dx,dy,depth+1, probability * probabilities[idx])
        visited.remove((dx,dy))

DFS(0,0,0,1)
print(ans)

