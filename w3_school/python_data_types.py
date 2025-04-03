# Integer (whole number)
num = 23
print("Integer:", num)

# Float (decimal number)
decimal_num = 5.1
print("Float:", decimal_num)

# String (sequence of characters)
greeting = "Hello, World!"
print("String:", greeting)

# Boolean (True or False)
is_active = True
print("Boolean:", is_active)

# List (ordered, mutable collection of elements)
fruits = ["kiwi", "banana", "strawberry"]
print("List:", fruits)

# Tuple (ordered, immutable collection of elements)
coordinates = (10, 20)
print("Tuple:", coordinates)

# Set (unordered, mutable collection of unique elements)
unique_numbers = {1, 2, 3, 4, 5}
print("Set:", unique_numbers)

# Dictionary (key-value pairs)
person = {
    "name": "Mert",
    "age": 32,
    "city": "Istanbul"
}
print("Dictionary:", person)

# Data Type Conversions
# Converting from Integer to Float
num_as_float = float(num)
print("Integer to Float:", num_as_float)

# Converting from Float to Integer
decimal_as_int = int(decimal_num)
print("Float to Integer:", decimal_as_int)

# Converting from String to Integer
str_num = "100"
str_to_int = int(str_num)
print("String to Integer:", str_to_int)

# Converting from Integer to String
int_as_str = str(num)
print("Integer to String:", int_as_str)

# Checking the type of data
print("\nData Types:")
print("Type of num:", type(num))
print("Type of decimal_num:", type(decimal_num))
print("Type of greeting:", type(greeting))
print("Type of is_active:", type(is_active))
print("Type of fruits:", type(fruits))
print("Type of coordinates:", type(coordinates))
print("Type of unique_numbers:", type(unique_numbers))
print("Type of person:", type(person))

