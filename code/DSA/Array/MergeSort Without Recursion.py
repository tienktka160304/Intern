def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def mergeSort(a):
    step = 1 #start with sub-array of length 1
    length = len(a)
    
    while step < length:
        for i in range(0, length, 2 * step):
            left = a[i: i + step]
            right = a[i + step: i + 2 * step]
            
            merged = merge(left, right)
            
            #place the merged array back into the original array
            for j, val in enumerate(merged):
                a[i + j] = val
                
        step *= 2 #double the sub-array length.
    return a

a = [3, 7, 6, -10, 15, 23.5, 55, -13]
print(mergeSort(a))