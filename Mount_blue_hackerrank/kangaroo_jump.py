def check_kangaroo(x1,v1,x2,v2):
    if v2 >= v1:        # v2 = v1  => 0 3 1 3
        return "NO"
    # while x1 < x2:
    #     x1 += v1
    #     x2 += v2
    #     if x1 == x2:
    #         return "YES"
    if ((x2-x1)%(v1-v2) == 0):
        return "YES"
    return "NO"

arr = list(map(int, input().split()))
x1 = arr[0]
v1 = arr[1]
x2 = arr[2]
v2 = arr[3]
print(check_kangaroo(x1,v1,x2,v2))