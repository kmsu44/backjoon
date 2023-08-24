from collections import deque
import copy


def BFS(sheep, wolf, info, tree):
    global possible
    q = deque()
    q.append((0, copy.deepcopy(sheep), copy.deepcopy(wolf)))
    while q:
        node, tmpsheep, tmpwolf = q.popleft()
        # print(node, tmpsheep, tmpwolf)
        
        if len(tmpsheep) == len(tmpwolf):
            continue
        if len(tmpsheep) > len(sheep):
            possible.append([tmpsheep, tmpwolf])
        for child in tree[node]:
            if info[child] == 0:
                if child in tmpsheep:
                    q.append((child, copy.deepcopy(
                        tmpsheep), copy.deepcopy(tmpwolf)))
                else:
                    tmpsheep.add(child)
                    q.append((child, copy.deepcopy(
                        tmpsheep), copy.deepcopy(tmpwolf)))
                    tmpsheep.remove(child)

            else:
                if child in tmpwolf:
                    q.append((child, copy.deepcopy(
                        tmpsheep), copy.deepcopy(tmpwolf)))
                else:
                    tmpwolf.add(child)
                    q.append((child, copy.deepcopy(
                        tmpsheep), copy.deepcopy(tmpwolf)))
                    tmpwolf.remove(child)


def solution(info, edges):
    global possible
    tree = [[] for _ in range(len(info))]
    for parent, child in edges:
        tree[parent].append(child)
    sheep = set([0])
    wolf = set()
    answer = len(sheep)
    c = 0
    possible = [[sheep, wolf]]
    answer = len(sheep)
    while possible:
        # print('sheep', sheep, wolf)
        sheep, wolf = possible.pop()
        answer = max(answer, len(sheep))
        BFS(sheep, wolf, info, tree)

    return answer

