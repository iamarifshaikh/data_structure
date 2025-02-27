# 1️⃣ What is a Dictionary?
# A dictionary is an unordered, mutable collection of key-value pairs.
# It allows fast lookups, insertions, and deletions based on keys.

# 🔹 Keys must be unique
# 🔹 Values can be duplicated

# 2️⃣ Creating a dictionary
# 1.Using Curly Braces
person = {"Name":"Arif","Age":21,"City":"Mumbai"}
print(person)

# 2. Using dict() constructor
person2 = dict(name="Abrar",age=20,city="Kolkata")
print(person2)

# 3. Using Tuples
pairs = [("name","Afzal"),("age",19),("city","Tamil")]
person3 = dict(pairs)
print(person3)

# 3️⃣ Accessing a dictionary elements

# 1. Using Square "[]" brackets
print(person["Name"])
# ❌ If the key is not found, it raises a KeyError

# 2. Using .get() (Safer way) -
print(person.get("age"))
print(person.get("gender","Not Specified"))
# ✅ Prevents errors by returning a default value if the key is missing.

# 4️⃣ Modifying a Dictionary
# 🔹 Adding or Updating Key-Value Pairs

person["city"] = "London"
person["age"] = 31
print(person)

# 5️⃣ Removing Elements from a Dictionary

# 🔹 Using pop()
age = person.pop("age")
print(age)
print(person)
# ❌ Raises a KeyError if the key is missing (unless a default is provided)

# 🔹 Using del
del person["city"]
print(person)
# ❌ Raises a KeyError if the key does not exist.

# 🔹 Using clear()
person.clear()
print(person) 
# ✅ Removes all key-value pairs

# 6️⃣ Iterating Over a Dictionary

# 🔹 Looping Over Keys
for key in person2:
    print(key,end=" ")

# 🔹 Looping Over Values
for value in person2.values():
    print(value)    

# 🔹 Looping Over Key-Value Pairs (items())
for key,value in person2.items():
    print(f"{key} : {value}")
    
# 8️⃣ Nested Dictionaries (Dictionaries Inside Dictionaries)
friends ={
    "Afzal" :{"age":21,"city":"Mumbai"},
    "Abrar": {"age":21,"city":"Gujrat"}
}
print(friends)

# 9️⃣ Checking If a Key Exists
# 🔹 Using in

print("name" in person2)
print("age" in person)

# 🔟 Dictionary Comprehension (Advanced)
squares = {x: x ** 1 for x in range(1,6)}
print(squares)