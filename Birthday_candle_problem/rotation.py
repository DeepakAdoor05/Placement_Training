def candle_selection(n_c,arr,n_r):
    for i in range(n_r):        # Rotation method need to be changed for efficiency
        temp = arr.pop(0)
        arr.append(temp)
    print(arr)
    value = arr[n_c//2]
    if value == min(arr):
        sorted_arr = sorted(arr)
        print(sorted_arr)
        next_larger_index = sorted_arr.index(value) + 1
        print(sorted_arr[next_larger_index])
    # elif value == max(arr):
    #     print(value)
    else:
        print(value)

n_candles = int(input())
arr = list(map(int, input().split(",")))
n_rotations = int(input())
candle_selection(n_candles,arr,n_rotations)