# задача с билетиком
#   abcdef
n = int(input("Введите 6-ти значное число : "))
# n - 38591 f - 6
n, f = divmod(n,10)
# n - 3859 f = 6 e = 1
n, e = divmod(n,10)
n, d = divmod(n,10)
n, c = divmod(n,10)
n, b = divmod(n,10)
n, a = divmod(n,10)
summ1 = f + e + d
summ2 = a + b + c
if summ1 == summ2:
    print("YES")
else:
    print("NO")
