str1 = input()
str2 = input()

a = int(str1)
b = int(str2)
p1 = a + b
p2 = a - b
p3 = a * b
p4 = a / b
p4 = "%f" % p4
print(f'{a} + {b} = {p1}')
print(f'{a} - {b} = {p2}')
print(f'{a} * {b} = {p3}')
print(f'{a} / {b} = {p4}')