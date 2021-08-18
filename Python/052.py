N = int(input())

A = [[] for i in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))

mod = 10 ** 9 + 7

total = []

for i in range(N):
    total.append(sum(A[i]))

ans = 1

for i in range(N):
    ans *= total[i]

print(ans%mod)