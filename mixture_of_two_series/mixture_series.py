def Fibonacci(n):
    first = 1
    second = 1
    fib_count = 2
    if n == 1:
        return first
    elif n == 2:
        return second
    else:
        while fib_count < n:
            third = first + second
            first = second
            second = third 
            fib_count += 1
        return third
    
    
def nth_prime(n):
    def is_prime(num):
        flag = True
        if num > 1:
            for i in range(2,num):
                if (num%i) == 0:
                    flag = False
                    break
            return flag
        return False
    prime_count = 0
    number = 2
    while True:
        if is_prime(number):
            prime_count += 1
        if prime_count == n:
            break
        number += 1
    return number

#   Optimized code
# def nth_prime(n):
#     def is_prime(num):
#         if num < 2:
#             return False
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True

#     prime_count = 0
#     number = 1
#     while prime_count < n:
#         number += 1
#         if is_prime(number):
#             prime_count += 1
#     return number

        
n = int(input())
if n%2 == 0:
    value = n//2
    solution = nth_prime(value)

else:
    value = (n +1)//2
    solution = Fibonacci(value)
print(solution)