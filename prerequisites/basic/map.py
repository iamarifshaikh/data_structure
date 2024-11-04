class SimpleMap:
    def __init__(self):
        self.data = [] # This will store the key value pairs as tuple

    def put(self,key,value):
        # Check if the key already exists, and update its value if it does
        for i, (k,v) in enumerate(self.data):
            if k == key:
                self.data[i] = (key,value)
                return
            
             # If the key doesn't exist, append a new key-value pair
        self.data.append((key,value))

    def get(self,key):
        for k,v in self.data:
            if k == key:
                return v # return the value associate to the key
        
        return None # Return None if the key is not found
    
    def remove(self,key):
        for i,(k,v) in enumerate(self.data):
            if k == key:
                del self.data[i]
                return

    def contains(self,key):
        for k, _ in self.data:
            if k == key:
                return True
        return False

my_map = SimpleMap()
my_map.put("apple", 1)
my_map.put("banana", 2)
print(my_map.data)  # Output: [('apple', 1), ('banana', 2)]
print(my_map.get("apple"))  # Output: 1
print(my_map.get("orange"))  # Output: None
my_map.remove("apple")
print(my_map.data)  # Output: [('banana', 2)]
print(my_map.contains("banana"))  # Output: True