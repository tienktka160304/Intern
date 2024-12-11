def partition (a, low, high):
    pivot = a[high] # pivot  = last element
    i = low - 1     # lượng elements <= pivot (lower)
    for j in range(low,high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i] # cho a[j] về vị trí nhỏ nhất 
            
    a[i + 1], a[high] = a[high], a[i + 1] # change pivot
    return i + 1

def quicksort(a, low, high):
    if low < high: 
        pivot = partition(a, low, high)
        quicksort(a, low, pivot - 1) #quicksort the left pivot
        quicksort(a, pivot + 1, high)#quicksort the right pivot

a = [64, 34, 25, 12, 22, 11, 90, 5] 
n = len(a) - 1
quicksort(a, 0, n)
print(a)