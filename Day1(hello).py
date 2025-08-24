# Introduction
# Day 1 - 7DaysOfPython Challenge
print("hello")
# Basic arithmetic operations in Python
print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)->Divides and returns the largest whole number (integer) less than or equal to the result

# Demonstration of different data types in Python
print(type(10))                  # Int (--- -1 ,0 ,1 ---)
print(type(3.14))                # Float(--- -1.0 , 0.0 , 1.0 ---)
print(type(1 + 6j))              # Complex-> Contains a real and an imaginary part
print(type('Aryan'))             # String-> Sequence of characters enclosed in single (' ') or double (" ") quotes
print(type([1, 2, 3]))           # List-> Ordered, mutable (changeable) collection. Can store multiple types of data.
print(type({'name':'Aryan'}))    # Dictionary-> Unordered collection of key-value pairs
print(type({9.8, 3.14, 2.7}))    # Set->Unordered, mutable collection of unique elements (no duplicates allowed)
print(type((9.8, 3.14, 2.7)))    # Tuple-> Ordered, immutable collection. Similar to list but cannot be changed after creation.
print(type(3 == 3))              # Bool-> Represents logical values True or False
print(type(3 >= 3))              # Bool-> Represents logical values True or False

''' Variables in Python -> A variable is like a container that stores a value.
 In Python, you don't need to declare the type of a variable explicitly(maually).
 Python is dynamically typed → it automatically understands the type.'''

# Example of single variable assignments
first_name = 'Aryan'       # string → sequence of characters
last_name = 'Sadotra'      # string
country = 'India'          # string
city = 'Jammu'             # string
age = 19                   # integer → whole number
is_married = False         # boolean → True/False values
# A list variable: stores multiple ordered values (can be different types)
skills = ['HTML', 'CSS', 'Python', 'C', 'Web Development']
# A dictionary variable: stores key-value pairs (like a real-world dictionary)
person_info = {
    'firstname': 'Aryan',
    'lastname': 'Sadotra',
    'country': 'India',
    'city': 'Jammu'
}
# Printing values stored in variables
print('First name:', first_name)                  # Output: Aryan
print('First name length:', len(first_name))      # len() returns number of characters → 5
print('Last name:', last_name)                    # Output: Sadotra
print('Last name length:', len(last_name))        # Output: 7
print('Country:', country)                        # Output: India
print('City:', city)                              # Output: Jammu
print('Age:', age)                                # Output: 19
print('Married:', is_married)                     # Output: False
print('Skills:', skills)                          # Output: ['HTML', 'CSS', 'Python', 'C', 'Web Development']
print('Person information:', person_info)         # Output: {'firstname': 'Aryan', 'lastname': 'Sadotra', ...}

# Declaring multiple variables in one line
# Python allows unpacking multiple values into multiple variables in a single line
first_name, last_name, country, age, is_married = 'Aryan', 'Sadotra', 'India', 19, False

# Printing after multiple assignment
print(first_name, last_name, country, age, is_married)
# Output: Aryan Sadotra India 19 False

# More detailed print
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)
print('Married:', is_married)

# ==========================================
# Arithmetic & Comparison Operations in Python
# ==========================================

# -------------------------------
# Integers (Basic Arithmetic → +, -, *, /, //, %, **)
# -------------------------------
print("Addition (1 + 2):", 1 + 2)              # 3
print("Subtraction (2 - 1):", 2 - 1)           # 1
print("Multiplication (2 * 3):", 2 * 3)        # 6
print("Division (4 / 2):", 4 / 2)              # 2.0 (always float in Python)
print("Division (7 / 2):", 7 / 2)              # 3.5
print("Floor Division (7 // 2):", 7 // 2)      # 3 (drops the decimal part)
print("Modulus (3 % 2):", 3 % 2)               # 1 (remainder of division)
print("Exponentiation (3 ** 2):", 3 ** 2)      # 9 (3 raised to power 2)

# Floating Numbers
print("Floating Number, PI:", 3.14)
print("Floating Number, Gravity:", 9.81)

# Complex Numbers
print("Complex number:", 1 + 1j)
print("Multiplying Complex Numbers:", (1 + 1j) * (1 - 1j))  # 2 (a² - b² formula)


# Declaring variables
a = 3  # integer
b = 2  # integer

# Arithmetic with variables
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# Printing results clearly
print("a + b =", total)
print("a - b =", diff)
print("a * b =", product)
print("a / b =", division)
print("a % b =", remainder)
print("a // b =", floor_division)
print("a ** b =", exponential)

# More Arithmetic Examples
num_one = 3
num_two = 4

print("Total:", num_one + num_two)
print("Difference:", num_two - num_one)
print("Product:", num_one * num_two)
print("Division:", num_two / num_one)
print("Remainder:", num_two % num_one)

# Real-Life Examples

# Area of a Circle: π * r²
radius = 10
area_of_circle = 3.14 * radius ** 2
print("Area of Circle:", area_of_circle)

# Area of a Rectangle: length * width
length = 10
width = 20
area_of_rectangle = length * width
print("Area of Rectangle:", area_of_rectangle)

# Weight of an object: mass * gravity
mass = 75
gravity = 9.81
weight = mass * gravity
print("Weight:", weight, "N")

# Comparison Operators → (==, !=, >, <, >=, <=)
print("3 > 2:", 3 > 2)       # True
print("3 >= 2:", 3 >= 2)     # True
print("3 < 2:", 3 < 2)       # False
print("2 <= 3:", 2 <= 3)     # True
print("3 == 2:", 3 == 2)     # False
print("3 != 2:", 3 != 2)     # True

# Comparing string lengths
print("len('mango') == len('avocado'):", len("mango") == len("avocado"))   # False
print("len('mango') < len('avocado'):", len("mango") < len("avocado"))     # True
print("len('milk') == len('meat'):", len("milk") == len("meat"))           # True

# Boolean Operations->( true or false )
print("True == True:", True == True)
print("True == False:", True == False)
print("False == False:", False == False)

print("True and True:", True and True)     # Both must be True
print("True or False:", True or False)     # At least one True

# Identity (is, is not) & Membership Operators (in, not in)
print("1 is 1:", 1 is 1)                       # True
print("1 is not 2:", 1 is not 2)               # True
print("'A' in 'Aryan':", 'A' in 'Aryan')       # True
print("'B' in 'Aryan':", 'B' in 'Aryan')       # False
print("'coding' in 'coding for all':", 'coding' in 'coding for all') # True
print("'a' in 'an':", 'a' in 'an')             # True
print("4 is 2 ** 2:", 4 is 2 ** 2)             # True

# Logical Operators-> (and, or, not)
print("3 > 2 and 4 > 3:", 3 > 2 and 4 > 3)     # True
print("3 > 2 and 4 < 3:", 3 > 2 and 4 < 3)     # False
print("3 > 2 or 4 < 3:", 3 > 2 or 4 < 3)       # True
print("not 3 > 2:", not 3 > 2)                 # False
print("not True:", not True)                   # False
print("not False:", not False)                 # True

''' ---------------- STRING BASICS ----------------
   String is a sequence of characters enclosed in either:
 - Single quotes (' ')
 - Double quotes (" ")
 - Triple quotes (''' ''' or """ """) for multi-line text'''

# ---------------- SINGLE CHARACTER STRING ----------------
letter = 'P'   # Here 'P' is a string with just one character
print(letter)  # Output: P

# len() gives the number of characters in a string
print(len(letter))  # Output: 1 (since there’s only one character: 'P')

# ---------------- FULL STRING ----------------
# Strings can hold words, sentences, or multiple characters
greeting = 'Hello, World!'  
print(greeting)     # Output: Hello, World!
print(len(greeting)) # Output: 13 (counts every character including space and !)

# ---------------- STRING SENTENCE ----------------
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)  
# Output: I hope you are enjoying 30 days of python challenge

# ---------------- THINGS TO KNOW ABOUT STRINGS ----------------
# 1. Strings are IMMUTABLE → once created, they cannot be changed directly.
#    Example: you cannot replace a single character by assigning directly.
# 2. Strings support INDEXING → to access characters using position (0-based index).
#    Example: greeting[0] → 'H'
# 3. Strings support SLICING → extract parts of a string.
#    Example: greeting[0:5] → 'Hello'
# 4. Strings can be CONCATENATED (+) or REPEATED (*).
#    Example: 'Hi ' + 'Python' → 'Hi Python'
#             'Ha' * 3 → 'HaHaHa'
# 5. Strings are used heavily in INPUT/OUTPUT and TEXT PROCESSING.

# ---------------- COMMENT TYPES ----------------
# Single-line comment → starts with #
# Multi-line comment → enclosed in ''' or """
