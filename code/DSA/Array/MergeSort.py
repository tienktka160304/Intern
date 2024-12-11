def mergeSort(a):
    if len(a) <= 1:
        return a
    
    mid = len(a) // 2
    leftHalf = a[:mid]  #array left half
    rightHalf = a[mid:] # array right half
    
    sortedLeft = mergeSort(leftHalf)    # split smaller
    sortedRight = mergeSort(rightHalf) #split smaller
    
    return merge(sortedRight, sortedLeft)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]: # so sánh từ vị trí đầu tiên l[0] vs r[0]
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

#the value of left[] and right[] are compared
    result.extend(left[i:])     # Put all values of left into the rightmost result
    result.extend(right[j:])    # Put all values of right into the rightmost result
    
    return result
 
a = [3434,34 ,353,4, 523,234 ,22,2]
mergeSort(a)
print(mergeSort(a))