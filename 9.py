a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
s = 0
for x in range(1001):
    if x != e and (a * x ** 3 + b * x ** 2 + c * x + d) == 0:
        s += 1
print(s)
