def bonAppetit(bill, k, b):
    bill.pop(k)
    b_actual = sum(bill) // 2  # Calculate the actual amount Anna should pay
    if b == b_actual:
        print("Bon Appetit")
    else:
        print(b-b_actual)

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())
bonAppetit(bill, k, b)

# Sample Input 0

# 4 1
# 3 10 2 9
# 12

# Sample Output 0
# 5

# Sample Input 1
# 4 1
# 3 10 2 9
# 7

# Sample Output 1
# Bon Appetit