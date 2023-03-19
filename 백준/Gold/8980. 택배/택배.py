n, truck_weight = map(int, input().split())
k = int(input())
info = [list(map(int, input().split())) for _ in range(k)]

info.sort(key=lambda x: [x[0], x[1]])
res = 0
truck = {}
index = 0
for position in range(1, n+1):
    remove_list = []
    for trunk_index in truck:
        r, w = truck[trunk_index]
        if position == r:
            res += w
            remove_list.append(trunk_index)
    for remove in remove_list:
        del truck[remove]
    for info_idx, info_data in enumerate(info):
        s, r, w = info_data
        if s == position:
            t = 0
            for truck_index in truck:
                ts, tw = truck[truck_index]
                t += tw
            # 트럭 용량이 남았을 경우 트럭에 짐을 실는다.
            # 전부 담을 수 있으면 전부 담기
            if t + w <= truck_weight:
                truck[index] = [r, w]
                index += 1
            # 부분만 담기
            else:
                # 부분적으로 남는 부분이 있으면 담기
                if t < truck_weight:
                    rest = truck_weight - t
                    truck[index] = [r, rest]
                    index += 1
                    w -= rest
                # 더 나은 경우 배달 취소 하기
                for truck_index in list(truck):
                    tr, tw = truck[truck_index]
                    if r <= tr:
                        if w < tw:
                            truck[truck_index][1] -= w
                            truck[index] = [r, w]
                            index += 1
                        elif w == tw:
                            truck[truck_index][0] = r
                        # w > tw
                        else:
                            truck[truck_index][0] = r
print(res)
