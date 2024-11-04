class SimpleSet:
    def __init__(self):
        self.data = [] # This will store the unique elements

    def add(self,element):
        if element not in self.data: # Ensure the element is unique
            self.data.append(element)    
    
    def remove(self,element):
        for i,e in enumerate(self.data):
            if e == element:
                del self.data[i] # remove the element
                return
    
    def contains(self,element):
        return element in self.data
    
    def __str__(self):
        return str(self.data)  # For easy viewing of the contents
    
# Example usage
my_set = SimpleSet()
my_set.add(1)
my_set.add(2)
my_set.add(1)  # Duplicates are ignored
print(my_set)  # Output: [1, 2]
print(my_set.contains(2))  # Output: True
my_set.remove(1)
print(my_set)  # Output: [2]
print(my_set.contains(1))  # Output: False