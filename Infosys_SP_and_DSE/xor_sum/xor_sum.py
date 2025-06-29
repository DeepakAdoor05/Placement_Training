def xor_sum(k,arr):
    xor_sum = sum(arr)
    for i in range(k):
        s = 0
        for j in arr:
            s += i^j    # xor symbol is "^"  (000^001 + 000^110 + 000^011 => 1+6+3 => 10 which is sum of array itself)
        if s > xor_sum:
            xor_sum = s
    return xor_sum

n = 3
k = 7
arr = [1,6,3]
print(xor_sum(k,arr))
