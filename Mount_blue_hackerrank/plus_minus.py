def plusMinus(arr):
    positive = negative = zeroes = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zeroes +=1
    print(f'{positive/len(arr):.6f}')
    print(f'{negative/len(arr):.6f}')
    print(f'{zeroes/len(arr):.6f}')

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
plusMinus(arr)

# Sample Input
# 5
# 1 1 0 -1 -1

# Sample Output
# 0.400000
# 0.400000
# 0.200000