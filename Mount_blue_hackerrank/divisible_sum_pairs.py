def divisibleSumPairs(n, k, ar):
    pair_count = 0
    for i in range(n):
        for j in range(1,n):
            if i<j and (ar[i]+ar[j])%k==0:
                pair_count += 1
    return pair_count

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
ar = list(map(int, input().rstrip().split()))
result = divisibleSumPairs(n, k, ar)
print(result)

# Sample Input

# STDIN           Function
# -----           --------
# 6 3             n = 6, k = 3
# 1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]

# Sample Output
#  5