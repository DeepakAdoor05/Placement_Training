def miniMaxSum(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    min_sum = sum(sorted_arr[:n-1])
    max_sum = sum(sorted_arr[1:])
    print(f'{min_sum} {max_sum}')

arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)

# Sample Input
# 1 2 3 4 5

# Sample Output
# 10 14