a = []

for x in range(int(input())):
    a.append(input())

n = len(a)
for t in range(n):
    a[t] = int(a[t])

for i in range(1,n):
    insert_index = i  # xét từng value của unsorted array
    crt_idx = a[i]     #copy value
    for j in range(i - 1, -1, -1): #xét từ phải qua trái (lớn đến bé) của mảng đã đc sort
        if a[j] > crt_idx:
            a[j+1] = a[j]   # shift những values > crt index
            insert_index = j
        else:
            break
    a[insert_index] = crt_idx    # insert value vào vị trí đúng của sorted array

print(a)