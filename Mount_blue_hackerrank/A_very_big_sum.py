def aVeryBigSum(ar):
    return sum(ar)

ar_count = int(input().strip())
ar = list(map(int, input().rstrip().split()))
print(aVeryBigSum(ar))

# STDIN
# -----
# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005   
# Output

# 5000000015