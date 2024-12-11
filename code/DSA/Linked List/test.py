import sys

n = 2

print(sys.getsizeof(n)) #Size of integer n(2) = 28 (bytes)

print(hex(id(n)))       #Address to n(2) = 0x7ff9b30c09d8

print(sys.getsizeof(id(n))) #Size of the address to n(2) = 32 (bytes)