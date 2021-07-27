def binary_search(data, value):
    left = 0 
    right = len(data) - 1 
    while left <= right:
        mid = (left + right) // 2
        if value == data[mid]:
            return mid
        elif value > data[mid]:
            left = mid + 1  
        else:
            right = mid - 1
    return left


N = int(input())
A = list(map(int, input().split()))

A.sort()

Q = int(input())
B = []
for i in range(Q):
    B.append(int(input()))

for i in range(Q):
    left = binary_search(A, B[i])
    if left == len(A):
        print(B[i] - A[left-1])
    elif left == 0:
        print(abs(A[left] - B[i]))
    else:
        print(min(abs(A[left] - B[i]), abs(B[i] - A[left-1])))