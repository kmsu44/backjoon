import sys
from sys import stdin

input = stdin.readline

s1 = input().strip()
s2 = input().strip()


def get_lcs(s1: str, s2: str) -> int:
    prev = [0] * (len(s2) + 1)
    curr = [0] * (len(s2) + 1)

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(curr[j-1], prev[j])

        prev, curr = curr, prev

    return prev[len(s2)]


print(get_lcs(s1, s2))


