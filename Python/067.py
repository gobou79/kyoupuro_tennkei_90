from collections import deque

N, K = map(int, input().split())

def henkan(x):
    a = 0
    d = deque()
    for i in range(len(x)):
        a += pow(8, i) * x[-(i+1)]
    
    while a > 0:
        d.appendleft(a % 9)
        a = a // 9
    return d

n = list(str(N))
if N == 0:
    print(0)
else:
    for i in range(len(n)):
        n[i] = int(n[i])

    for i in range(K):
        d = henkan(n)
        for j in range(len(d)):
            if d[j] == 8:
                d[j] = 5    
        n = d
        
    ans = map(str, n)
    print(''.join(ans))
