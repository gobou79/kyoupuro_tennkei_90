N, M = map(int, input().split())

d = [0 for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    if a < b:
        d[b-1] += 1   
    else:
        d[a-1] += 1    

ans = 0

for i in range(N):
    if d[i] == 1:
        ans += 1 

print(ans)