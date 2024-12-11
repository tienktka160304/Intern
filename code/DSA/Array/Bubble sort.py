array = []
for x in range(5):
    array.append(input())
n = len(array)
for t in range(n):
    array[t] = int(array[t])  #Change the datatype to int
for i in range(n-1):
    Swapped = False
    for j in range(n-i-1): 
        if array[j] > array[j + 1]: 
            array[j], array[j + 1] = array[j + 1], array[j]
            Swapped = True
    if not Swapped : # Swapped == False
        break
print(array)
#output = [6, 7, 8, 23, 45, 46, 56]