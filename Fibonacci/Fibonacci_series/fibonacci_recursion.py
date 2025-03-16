def fib_rec(n):
    if n <= 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)
    
number = 5
sum = 0
for i in range(number):
    print(fib_rec(i),end = " ")              # (Display the fibonacci series,  0 1 1 2 3)
#     sum += fib_rec(i)
# print("\n",sum)          # 0+1+1+2+3 = 7 (Display the Sum of fibonacci series)
# print(fib_rec(3))     This will give the nth term (starts with 0) 3rd term will be '2'.