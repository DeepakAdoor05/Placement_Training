def quickSort(arr):
    # Write your code here
    pivot = arr[0]
    left = []
    right = []
    result = []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal = [pivot]
    result = left+equal+right
    return result

n = int(input().strip())    # n = 5                     # n = 5
arr = list(map(int, input().rstrip().split()))          # 4 5 3 7 2
result = quickSort(arr)                                 # [3, 2, 4, 5, 7]
print(' '.join(map(str, result)))                       # 3 2 4 5 7