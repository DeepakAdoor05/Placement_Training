def getTotalX(a, b):
    # Write your code here
    count = 0
    for i in range(max(a),min(b)+1):
        # print(i)
        if all(i%x == 0 for x in a) and all(y%i == 0 for y in b):
            count += 1
    return count

    # using list comprehension
    # elements = [i for i in range(a[-1],b[0]+1) if all(i%x == 0 for x in a) and all(y%i == 0 for y in b)]
    # print(elements)   
    # return len(elements)

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
brr = list(map(int, input().rstrip().split()))
total = getTotalX(arr, brr)
print(total)