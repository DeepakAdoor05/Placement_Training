def birthday(s, d, m):
    count = 0
    if len(s) == 1 and s[0] == d:
        count = 1
    else:
        for i in range(len(s)-2):
            sum_value = sum(s[i:i+m])
            if sum_value == d:
                count += 1
    return count

n = int(input().strip())
s = list(map(int, input().rstrip().split()))
first_multiple_input = input().rstrip().split()
d = int(first_multiple_input[0])
m = int(first_multiple_input[1])
print(birthday(s, d, m))

# Sample Input 0
# 5
# 1 2 1 3 2
# 3 2

# Sample Output 0
# 2