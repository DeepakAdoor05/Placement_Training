a = [10,20,20,10,10,30,50,10,20]
b = set(a)
v_count = 0
for i in b:
    value = a.count(i)//2
    v_count += value
print(v_count)