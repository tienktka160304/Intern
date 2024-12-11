def bubbleSort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                
def radixSortWithBubbleSort(a):
    
    max_value = max(a)
    exp = 1
    
    while max_value // exp > 0:
        radix_array = [[], [], [], [], [], [], [], [], [], []]
        for num in a:
            radix_idx = (num // exp) % 10
            radix_array[radix_idx].append(num)
            
        for x in radix_array:
            bubbleSort(x) #sort values in radix-array
            
        i = 0
        for x in radix_array:   # x chạy từ đầu đến cuối radix array
            for num in x:
                a[i] = num  #nhập num vào a theo thứ tự 0 - max (do x đã đc sort)
                i += 1
                
        exp *= 10
    
a = [170, 45, 75, 90, 802, 24, 2, 66]
radixSortWithBubbleSort(a)
print(a)