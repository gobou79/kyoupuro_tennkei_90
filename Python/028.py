from collections import defaultdict

N = int(input())
imos = [[0 for i in range(1001)] for j in range(1001)]
for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    imos[ry][lx] -= 1
    imos[ly][rx] -= 1
    imos[ry][rx] += 1
    imos[ly][lx] += 1

for i in range(1001):
    for j in range(1, 1001):
        imos[i][j] = imos[i][j] + imos[i][j-1]

for j in range(1001):
    for i in range(1, 1001):
        imos[i][j] = imos[i][j] + imos[i-1][j]

ans = defaultdict(int)

for i in range(1001):
    for j in range(1001):
        if imos[i][j] > 0:
            ans[imos[i][j]] += 1

for i in range(1, N+1):
    print(ans[i])