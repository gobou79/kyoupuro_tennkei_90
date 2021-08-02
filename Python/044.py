from collections import deque

N, Q = map(int, input().split())
A = deque(list(map(int, input().split())))

for i in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        A[x-1], A[y-1] = A[y-1], A[x-1]
    elif t == 2:
        last = A.pop()
        A.appendleft(last)
    else:
        print(A[x-1])