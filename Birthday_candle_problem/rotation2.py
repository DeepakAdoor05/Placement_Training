def find_candle_to_gift(n, arr, r):     # wrong code rotation 2 goes instead of 3
    # Perform R rotations
    r = r % n  # To handle cases where r > n
    rotated_arr = arr[-r:] + arr[:-r]
    print(rotated_arr)
    # Find the middle candle
    middle_index = n // 2
    middle_candle = rotated_arr[middle_index]
    
    # Determine the candle to gift
    largest_candle = max(rotated_arr)
    smallest_candle = min(rotated_arr)
    
    if middle_candle == largest_candle:
        return largest_candle
    elif middle_candle == smallest_candle:
        # Find the next larger candle
        sorted_arr = sorted(rotated_arr)
        print(sorted_arr)
        next_larger_index = sorted_arr.index(smallest_candle) + 1
        print(next_larger_index)
        return sorted_arr[next_larger_index]
    else:
        return middle_candle

# Input
n = int(input("Enter the number of candles: "))
arr = []
print("Enter the sizes of the candles:")
for _ in range(n):
    arr.append(int(input()))
r = int(input("Enter the number of rotations: "))

# Output
result = find_candle_to_gift(n, arr, r)
print("Candle to gift:", result)