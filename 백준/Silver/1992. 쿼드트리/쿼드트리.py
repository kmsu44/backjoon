import sys
input = sys.stdin.readline
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
graph = [list(input()) for _ in range(n)]



def compact(n,x,y):
    s = 0
    for i in range(x,x+n):
        for j in range(y,y+n):
            s += int(graph[i][j])
    if s == 0:
        return '0'
    elif s == n*n:
        return '1'
    else:
        size = n // 2
        a = compact(size,x,y)
        b = compact(size,x,y+size)
        c = compact(size,x+size,y)
        d = compact(size,x+size,y+size)
        return '(' + a + b+ c+ d +')'
print(compact(n,0,0))