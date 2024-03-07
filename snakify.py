#a = input().split(" ")
a= "-9 29 -100 64 26 73 -96 28 -92 11 -14 -86 -54 -67".split(" ")
total = 0
for i in range(len(a)-1):
    if int(a[i-1]) + int(a[i+1]) < int(a[i]):
        total += 1

print(total)