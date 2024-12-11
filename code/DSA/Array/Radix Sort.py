a = [170, 45, 75, 90, 802, 24, 2, 66]
radix_A = [[], [], [], [], [], [], [], [], [], []]
max_value = max(a)
exp = 1  

while max_value // exp > 0:      #số vòng lặp theo số chữ số của max
    
    while len(a) > 0:       # move value from array to radix array
        value = a.pop()
        radix_idx = (value // exp) % 10     #để theo từng chữ số của mỗi lần lặp exp
        radix_A[radix_idx].append(value)
        
    for x in radix_A:       #để lấy các chữ số trong radix array ra và chèn vô array
        while len(x) > 0:
           value = x.pop()
           a.append(value)
    
    exp *= 10
    
print(a)