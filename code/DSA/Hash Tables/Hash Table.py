def hash_func(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char) # char -> int
#chuyển từng char của value sang unicode

    return sum_of_chars % 10 # module để lấy vị trí ( giá trị ) của value

def contain(name):
    index = hash_func(name)
    return Hash_table[index] == name
    # my_array[index] = None
    # return 

Hash_table = [None, 'Jones', None, 'Lisa', None, 'Bob', None, 'Siri', 'Pete', None]


# contain('Pete')
# print(my_array) #[None, 'Jones', None, 'Lisa', None, 'Bob', None, 'Siri', None, None]