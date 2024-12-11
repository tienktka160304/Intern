import time
start = time.time()
a = []
for i in range(10):
    a.append(input())
min = a[0]

for x in a:
    if min > x:
        min = x
end = time.time()
print(min)
print(end-start)