from collections import deque

N = int(input())
g = [[] for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

d = deque()
d.append(0)
dist = [-1 for i in range(N)]
dist[0] = 0

while d:
    v = d.popleft()
    for u in g[v]:
        if dist[u] != -1:
            continue
        else:
            dist[u] = dist[v]+1
            d.append(u)

white = []
black = []

for i in range(N):
    if dist[i] % 2 == 0:
        white.append(i+1)
    else:
        black.append(i+1)

if len(white) >= N // 2:
    print(*white[:N//2])
else:
    print(*black[:N//2])