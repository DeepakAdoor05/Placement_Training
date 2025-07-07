def sockMerchant(n, ar):
    # Write your code here
    count_pair = 0
    for i in set(ar):
        count_value = ar.count(i)
        count_pair += count_value//2
    return count_pair

n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
print(sockMerchant(n, ar))