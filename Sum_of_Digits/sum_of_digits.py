def digit_sum(num):
    sum = 0
    while num > 0:
        value = num %10
        sum += value
        num = num // 10
    return sum

print(digit_sum(1234))