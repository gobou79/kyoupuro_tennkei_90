N = int(input())
S = input()
cnt = 1
c = S[0]
ans = (1+N) * N // 2

for i in range(1, N):
    if c == S[i]:
        cnt += 1
    else:
        ans -= (1+cnt) * cnt // 2
        cnt = 1
        c = S[i]

ans -= (1+cnt) * cnt // 2
print(ans)