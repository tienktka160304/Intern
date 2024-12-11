class SimpleHashMap:
    def __init__(self, size = 100):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        
    def hash_function(self, key):
    # Sum only the numerical values of the key, ignoring non-numeric characters
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum % 10
    
    def put(self, key, value):
        #add or update a key-value pair
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
    #(k, v) pair is extracted (trích xuất) from the bucket
            if k == key:    #if security number = key
                bucket[i] = (key, value)    #update the existing key's value
                return
        bucket.append((key, value)) #add is key does not exist
            
    def get(self, key): #get value (name)
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None # key not found
    
    def remove (self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]   #remove the key-valie pair
                return
        
    def print_map(self):
        for index, bucket in enumerate(self.buckets):
            print(f'Bucket {index} : {bucket}')
            

hash_map = SimpleHashMap(size=10)

hash_map.put("123-4567", "Charlotte")
hash_map.put("123-4568", "Thomas")
hash_map.put("123-4569", "Jens")
hash_map.put("123-4570", "Peter")
hash_map.put("123-4571", "Lisa")
hash_map.put("123-4672", "Adele")
hash_map.put("123-4573", "Michaela")
hash_map.put("123-6574", "Bob")

hash_map.print_map()

# Demonstrating retrieval
print(hash_map.get("123-4570"))

hash_map.put("123-4570","James") #update

# Checking if Peter is still there
print(hash_map.get("123-4570"))