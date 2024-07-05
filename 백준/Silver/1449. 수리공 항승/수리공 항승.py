N, L = map(int,input().split())

repair_list = list(map(int,input().split()))
repair_list.sort()


tape_cnt = 1
start = repair_list[0]

for pos in repair_list[1:]:
    diff = pos-start + 1
    if diff <= L:
        continue
    else:
        start = pos
        tape_cnt += 1

print(tape_cnt)