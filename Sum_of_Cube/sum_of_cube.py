# TCS-NQT-2024-Question
def sum_of_cubes(start,end):
    sum = 0
    for i in range(start,end + 1):
        sum += i ** 3
    return sum

start,end = map(int, input().split(','))
print(sum_of_cubes(start,end))