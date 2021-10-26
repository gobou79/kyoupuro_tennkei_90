import bisect

N = int(input())
A = list(map(int, input().split()))

total = sum(A) / 10

A1 = A + A
B = []
ans = False

for i in range(len(A1)):
    if i == 0:
        B.append(A1[i])
    else:
        B.append(B[i-1] + A1[i])

for i in range(N):
    b_r = B[i] + total
    k = bisect.bisect_left(B, b_r)
    if B[k] == b_r:
        print("Yes")
        exit()

print("No")