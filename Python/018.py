import math

T = int(input())
L, X, Y = map(int, input().split())

Q = int(input())

E = []

for i in range(Q):
    e = int(input())
    E.append(e)

for i in range(Q):
    e = E[i]
    y = - L/2 * math.cos(math.radians((360/T)*e - 90))
    z = L/2 + L/2 * math.sin(math.radians((360/T)*e - 90))
    l = math.sqrt(X**2 + (Y - y)**2)
    print(math.degrees(math.atan2(z, l)))