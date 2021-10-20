N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = []
ans = 0
for i in range(N-1):
    B.append(A[i+1]-A[i])
    ans += abs(A[i+1] - A[i])

for i in range(Q):
    l, r, v = map(int, input().split())
    if l != 1 and r != N:
        ans -= abs(B[l-2]) + abs(B[r-1])
        B[l-2] += v
        B[r-1] -= v
        ans += abs(B[l-2]) + abs(B[r-1])
    elif r == N and l != 1:
        ans -= abs(B[l-2])
        B[l-2] += v
        ans += abs(B[l-2])
    elif l == 1 and r != N:
        ans -= abs(B[r-1])
        B[r-1] -= v
        ans += abs(B[r-1])

    print(ans)
