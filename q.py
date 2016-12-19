#1
a = [19, 17, 24, 1, 100, 25, 846, 39]
i = 0
min = a[i]
max = a[i]
while i < len(a):
    if a[i] < min:
        min = a[i]
    if a[i] > max:
        max = a[i]
    i = i + 1
print ("min =", min,"max =", max)

# 2
A = {0: 0, 1: 1}
def fib(n):
    if n in A:
        return A[n]
    A[n] = fib(n-1) + fib(n-2)
    return A[n]
print(fib(15))