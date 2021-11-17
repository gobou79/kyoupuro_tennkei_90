from collections import defaultdict

N, K = map(int, input().split())
a = list(map(int, input().split()))

d = defaultdict(int)
cnt = 0
index = 0
ans = K

for i in range(N):
    if d[a[i]] == 0:
        d[a[i]] += 1
        cnt += 1
    else:
        d[a[i]] += 1
    if cnt > K:
        if (i-index) > ans:
            ans = i - index
        for j in range(index, i):
            d[a[j]] -= 1  
            if d[a[j]] == 0:
                index = j+1
                cnt -= 1
                break

if (N-1) - index + 1 > ans:
    ans = (N-1) - index + 1
    print(ans)
else:
    print(ans)