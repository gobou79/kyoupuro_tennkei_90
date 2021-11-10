from collections import deque

N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

def BFS(G, start):
    d = deque()
    d.append(start)
    dist = [-1 for i in range(N)]
    dist[start] = 0
    while d:
        v = d.popleft()
        for u in G[v]:
            if dist[u] > -1:
                continue
            else:
                d.append(u)
                dist[u] = dist[v] + 1
    return dist

dist_first = BFS(G, 0)
max_value = max(dist_first)
index = dist_first.index(max_value)

dist_second = BFS(G, index)

print(max(dist_second)+1)
