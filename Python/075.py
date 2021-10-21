import math

N = int(input())
X = int(math.sqrt(N))
cnt = 0

for i in range(2, X+1):
    while N > i:
        if N % i == 0:
            cnt += 1
            N = N // i
        else:
            break

if N != 1:
    cnt += 1

for i in range(1000000):
    if 2 ** i >= cnt:
        print(i)
        break