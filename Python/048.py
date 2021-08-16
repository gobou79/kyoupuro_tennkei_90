N, K = map(int, input().split())

l = []

for i in range(N):
    a, b = map(int, input().split())
    l.append(b)
    l.append(a-b)

l.sort(reverse=True)
ans = 0

for i in range(K):
    ans += l[i]

print(ans)