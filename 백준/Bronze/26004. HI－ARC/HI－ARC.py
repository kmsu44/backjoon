n = int(input())
s = input()
answer = {'H': 0, 'I': 0, 'A': 0, 'R': 0, 'C': 0}
for i in s:
    if i in answer:
        answer[i] += 1


res = 100000
for i in answer:
    if answer[i] == 0:
        print(0)
        exit()
    else:
        res = min(res, answer[i])
print(res)
