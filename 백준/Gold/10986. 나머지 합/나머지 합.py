import sys
N, M = map(int, sys.stdin.readline().split()) # 2개
x = list(map(lambda x:x%M, map(int,sys.stdin.readline().split()))) # 여러개

cumulate_sum = [0]*len(x)
reminder_set = [0]*(M)

cumulate_sum[0] = x[0]

# reminder_set 배열 생성 : 나머지가 같은 것(0~M-1)끼리 개수를 카운트하는 배열
reminder_set[cumulate_sum[0]] += 1

for i in range(1, len(x)):
    cumulate_sum[i] += (cumulate_sum[i-1] + x[i]) % M
    reminder_set[cumulate_sum[i]] += 1

count = 0
for i in range(len(reminder_set)):
    temp = reminder_set[i]
    
    # 나머지가 0 인 경우는, 자기 자신 혼자 있어도 나머지 0이 됨
    if i == 0 :
        count += temp
    
    # 나머지 0~M-1 일 때 nC2 합하기
    count += int((temp)*(temp-1)/2)
    
print(count)