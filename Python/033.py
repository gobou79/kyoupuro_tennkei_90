import math

H, W = map(int, input().split())

if H == 1:
    print(W)
elif W == 1:
    print(H)
else:
    print(math.ceil(H/2) * math.ceil(W/2))