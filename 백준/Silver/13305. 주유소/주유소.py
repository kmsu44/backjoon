N = int(input())
distance = list(map(int,input().split()))
gas_station = list(map(int,input().split()))

def find_cheaper_station(idx):
    for i in range(idx+1,N):
        if  gas_station[i] < gas_station[idx]:
            return i
    return -1



cost = 0
cur = 0

while cur < N:
    next_charge = find_cheaper_station(cur)
    if next_charge == -1:
        remain_distance = sum(distance[cur:])
        cost += remain_distance * gas_station[cur]
        break
    else:
        remain_distance = sum(distance[cur:next_charge])
        cost += remain_distance * gas_station[cur]
        cur = next_charge
print(cost)