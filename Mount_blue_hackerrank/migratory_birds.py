def migratoryBirds(arr):
    min = 0
    for i in set(arr):
        value = arr.count(i)
        if value > min:
            min = value
            element = i
    return element

arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
print(migratoryBirds(arr))