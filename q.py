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