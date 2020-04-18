n = int(input())
sum1 = 0
for i in range(1, n + 1):
    sum1 += i
for i in range(n - 1):
    sum1 -= int(input())
print(sum1)
