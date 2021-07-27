from collections import defaultdict

N = int(input())
S = []
for i in range(N):
    S.append(input())

d = defaultdict(int)

for i in range(N):
    if d[S[i]] == 0:
        d[S[i]] = 1
        print(i+1)