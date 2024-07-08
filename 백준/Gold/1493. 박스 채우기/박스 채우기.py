length, width, height = map(int,input().split())
n = int(input())
cubes = [list(map(int,input().split())) for _ in range(n)]

cubes.sort(key=lambda x:-x[0])

total_cnt = 0
ans = 0
cur_len = 2 ** n

for a,b in cubes:
    # 현재 크기의 정육면체 갯수
    total_cnt *= 8
    cur_len = cur_len // 2
    fill_cnt = (length // cur_len) * (width // cur_len) * (height // cur_len) - total_cnt
    fill = min(fill_cnt,b)
    ans += fill
    total_cnt += fill

if total_cnt == length * width * height:
    print(ans)
else:
    print(-1)