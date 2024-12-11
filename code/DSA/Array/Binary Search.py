def BinarySearch(a, target_value):
    left = 0
    right = len(a) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if target_value == a[mid]:
            return mid

        if a[mid] < target_value:
            left = mid + 1
        else:
            right = mid - 1
        
    
    return -1

a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 15

print(BinarySearch(a, target))