from collections import deque

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())

S = []

for i in range(H):
    s = list(input())
    S.append(s)

dist = [[float('inf') for i in range(W)] for j in range(H)]
dist[rs-1][cs-1] = 0

dhdw = [(0, 1), (0, -1), (1, 0), (-1, 0)]

q = deque([(rs-1, cs-1)])

while q:
    h, w = q.popleft()
    if h==rt-1 and w==ct-1:
        break
    for dh, dw in dhdw:
        nh, nw = h + dh, w + dw
        while 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] > dist[h][w]:
            if dist[nh][nw] == float("inf"):
                q.append((nh, nw))
            dist[nh][nw] = dist[h][w] + 1
            nh += dh
            nw += dw

print(dist[rt-1][ct-1] - 1)