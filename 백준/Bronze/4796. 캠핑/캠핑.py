idx = 1
while True:
    L,P,V = map(int,input().split())
    if L==0 and P ==0 and V ==0:
        break
    q,r = divmod(V,P)
    res = q * L
    res += L if r >= L else r
    print(f"Case {idx}: {res}")
    idx+=1