def countingsort(a):
    max_value = max(a)      # find the max value
    count = [0] * (max_value + 1) # create counting array
    
    while len(a) > 0:
        num = a.pop(0)
        count[num] += 1
        
    for i in range(len(count)):
        while count[i] > 0:
            a.append(i)
            count[i] -= 1
            
    return a

arr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
print(countingsort(arr))