def binary_rearrange(a,b):
    if a.count('1') == b.count('1'):
        return "Yes"
    return "No"

num1 = '101'
num2 = '011'
print(binary_rearrange(num1,num2))