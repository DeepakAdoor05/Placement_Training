def fibonacci(num):
    first = 1
    second = 1
    fib_count = 2
    if num == 1:
        return first
    if num == 2:
        return second
    else:
        while fib_count < num:
            third = first + second
            first = second
            second = third
            fib_count += 1
        return third

print(fibonacci(6))