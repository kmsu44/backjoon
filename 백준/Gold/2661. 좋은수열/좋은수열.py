n = int(input())
answer = ''

def check_sub_sequence(sequence):
    if len(sequence) <= 2:
        return True
    idx = len(sequence)-1
    size = len(sequence) // 2
    for s in range(size):
        # print('idx',idx)
        a = ''.join(str(i) for i in sequence[idx-s:idx+1])
        b = ''.join(str(i) for i in sequence[idx-2*s-1:idx-s])
        # print('a',a)
        # print('b',b)
        if a == b:
            return False
    return True


def sol(n,sequence):
    global answer
    if answer != '':
        return
    if len(sequence) == n:
        answer = ''.join(str(i) for i in sequence)
        return
    for i in range(1,4):
        if sequence[-1] != i:
            sequence.append(i)
            if check_sub_sequence(sequence):
                sol(n,sequence)
            sequence.pop()
    
    
for i in range(1,4):
    sol(n,[i])
print(answer)




