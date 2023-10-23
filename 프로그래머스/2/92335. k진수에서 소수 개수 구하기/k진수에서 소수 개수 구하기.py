import math
def numberic(n,k):
    res = ''
    while n > 0:
        n,mod = divmod(n,k)
        res+=str(mod)
    return res[::-1]

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True
def solution(n, k):
    # 소수판별 에라토스테네스의 체
    n = n * k 
    primes = [True for _ in range(n+1)]
    for i in range(2, int(math.sqrt(n))+1):
        if primes[i]:
            for j in range(2*i, n+1, i):
                primes[j] = False
    
    string = numberic(n,k)
    cnt = 0
    
    for num in string.split('0'):
        if(num == '1' or num== ''):
            continue
        print(int(num))
        if(is_prime_number(int(num))):
            cnt+=1
            
        
    
    return cnt