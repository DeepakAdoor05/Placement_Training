def sum_of_tables(num):
    sum = 0
    for i in range(11):
        sum += num*i
    print(sum)
n = int(input())
sum_of_tables(n)