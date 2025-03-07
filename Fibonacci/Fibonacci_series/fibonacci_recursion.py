def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)
    
number = 5
for i in range(number):
    print(fib_rec(i))
# print(fib_rec(3))     This will give the nth term (starts with 0) 3rd term will be '2'.