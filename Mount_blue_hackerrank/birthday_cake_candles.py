def birthdayCakeCandles(candles):
    value = max(candles)
    return candles.count(value)

candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
print(birthdayCakeCandles(candles))

# Sample Input 0
# 4
# 3 2 1 3

# Sample Output 0
# 2