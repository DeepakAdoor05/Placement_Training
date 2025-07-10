def pageCount(n, p):
    l = p//2
    n = n+1 if n%2==0 else n    # if n is even, add 1 to make it odd
    r = (n-p)//2                # this eq is only working for odd n values
    return min(l,r)

n = int(input().strip())
p = int(input().strip())
print(pageCount(n, p))

# Sample Input 0
# 6
# 2

# Sample Output 0
# 1

# Sample Input 1
# 5
# 4

# Sample Output 1
# 0
