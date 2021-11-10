N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
    if i == 0:
        B.append(A[i])
    else:
        B.append(A[i]-A[i-1])
B.append(L - A[-1])

left = 0
right = L

while (right - left) > 1:
    mid = (left + right) // 2
    cnt = 0
    length = 0
    for i in range(N+1):
        length += B[i]
        if length >= mid:
            cnt += 1
            length = 0
    if cnt >= K+1:
        left = mid
    else:
        right = mid-1

if left == right:
    print(left)
else:
    cnt = 0
    length = 0
    for i in range(N+1):
        length += B[i]
        if length >= right:
            cnt += 1
            length = 0
    if cnt >= K+1:
        print(right)
    else:
        print(left)