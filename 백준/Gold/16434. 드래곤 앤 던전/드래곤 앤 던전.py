import sys
n, atk = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def can_clear(max_hp):
    cur_hp = max_hp
    cur_atk = atk
    for t,a,h in arr:
        if t == 1:
            if h <= cur_atk:
                continue
            r,c = divmod(h,cur_atk)
            cnt = r - 1 if c == 0 else r
            cur_hp -= cnt * a
            if cur_hp <= 0:
                return False
        else:
            cur_atk += a
            cur_hp += h
            if cur_hp > max_hp:
                cur_hp = max_hp
    return True

left, right = 1,sys.maxsize
while left <= right:
    max_hp = (left+right) // 2
    if can_clear(max_hp):
        right = max_hp - 1
        ans = max_hp
    else:
        left = max_hp + 1
print(ans)