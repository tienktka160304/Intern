my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa', 'Stuart'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

print(my_hash_set) 
# output = [[None], ['Jones'], [None], ['Lisa', 'Stuart'], [None], ['Bob'], [None], ['Siri'], ['Pete'], [None]]
def hash_func(value):
    return sum(ord(char) for char in value) % 10

def add(value):
    index = hash_func(value)
    bucket = my_hash_set[index]
    if value not in bucket:
        bucket.append(value)
        
def contain(value):
    index = hash_func(value)
    bucket = my_hash_set[index]
    return value in bucket

add('Stuart')

print(contain('Stuart')) #=> True