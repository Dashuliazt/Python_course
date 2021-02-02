import math
import random

var1 = 23
print(type(var1))
var1 = float(var1)
print(type(var1))
var2 = var1+var1
pi = math.pi
pi = round(pi, 2)
p = pow(pi, 5) // 3
a = pi * 3 % 2
rand_float1 = random.random()
rand_float2 = random.random()
rand_digit1 = random.randint(10, 40)
rand_digit2 = random.randint(-10, 10)
rand_choice = random.choice(range(50))
max_result = max(var1, var2, a, pi, p, rand_float1, rand_float2, rand_digit1,
                 rand_digit2, rand_choice)
min_result = min(var1, var2, a, pi, p, rand_float1, rand_float2, rand_digit1,
                 rand_digit2, rand_choice)
samp = random.sample(range(120), 10)






import string
a = string.ascii_letters + string.digits
print(a[0])
print(a[-1])
print(a[:8])
print(a[:3]+a[-3:])
g = a.index('H')
f = len(a)
h = a.replace('A', '0633750745')
k = a[::-1]
y = f/2
q = a[:30] + 'Dasha' + a[31:]
l = q.replace('Dasha', '')



