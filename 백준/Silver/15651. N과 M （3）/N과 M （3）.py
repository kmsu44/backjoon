n, m = map(int, input().split())


def BT(depth, route):
    if depth == m:
        print(*route)
        return
    for i in range(1, n+1):
        route.append(i)
        BT(depth+1, route)
        route.pop()


for i in range(1, n+1):
    BT(1, [i])
