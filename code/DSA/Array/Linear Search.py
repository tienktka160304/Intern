def linearSearch(a, target_value):
    for i in range(len(a)):
        if a[i] == target_value:
            return i
    
    return -1

a = [3, 7, 2, 9, 5]
target_value = 4
print(linearSearch(a, target_value))