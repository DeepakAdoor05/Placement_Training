from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in product(A,B):
    print(i,end="")

# print(list(product([1,2,3],[3,4])))
# o/p => [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]