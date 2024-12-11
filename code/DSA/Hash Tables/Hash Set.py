class SimpleHashSet:
    def __init__(self, size = 100):
        self.size = size
        self.buckets = [[] for _ in range(size)] #create a list of buckets, each a list
        
    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size #based on size to create buckets
    
    def add(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)
            
    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket
    
    def Remove(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)
            
    def print_set(self):
        for index, bucket in enumerate(self.buckets):
            print(f'Bucket {index}: {bucket}')
            #f : embed (nhúng) expressions inside string literals
            
hash_set = SimpleHashSet(size = 10)

hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")
         
hash_set.print_set()   

print(hash_set.contains('Peter'))
hash_set.Remove('Peter')
print(hash_set.contains('Peter'))
print(hash_set.hash_function('Adele'))
         
hash_set.print_set()   