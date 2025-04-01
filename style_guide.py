# 1. Naming Conventions
# Bad Example
Var = 10  # wrong: variable names should be lowercase with underscores

# Good Example
my_variable = 10  # correct: use lowercase with underscores

# 2. Indentation
# Bad Example
def bad_function():
    print("This is bad")  # wrong: no indentation

# Good Example
def good_function():
    print("This is correct")  # correct: properly indented

# 3. Line Length (should be <= 79 characters)
# Bad Example
def long_function(): 
    print("This line is way too long and should be broken into multiple lines for readability.")  # wrong

# Good Example
def good_function():
    print(
        "This line is properly broken into multiple lines for better readability."
    )  # correct

# 4. Spacing Around Operators
# Bad Example
x=5+ 3*2   # wrong: inconsistent spacing

# Good Example
x = 5 + 3 * 2  # correct: proper spacing around operators

# 5. Function and Class Naming
# Bad Example
def myFunction():  # wrong: should use snake_case
    pass

class my_class:  # wrong: class names should use PascalCase
    pass

# Good Example
def my_function():  # correct
    pass

class MyClass:  # correct
    pass

# 6. Imports
# Bad Example
import sys, os  # wrong: multiple imports on one line

# Good Example
import sys
import os  # correct: one import per line

# 7. Docstrings
# Bad Example
def no_doc():
    pass  # wrong: no docstring

# Good Example
def with_doc():
    """This function has a proper docstring."""
    pass  # correct

# 8. Comments
# Bad Example
x = 10  # defining x (not useful)

# Good Example
x = 10  # The number of items in stock

# 9. Avoid Unnecessary Whitespaces
# Bad Example
y = 42  

# Good Example
y = 42  # No extra trailing spaces

# 10. Constants Should Be Uppercase
# Bad Example
pi = 3.14  # wrong: should be uppercase

# Good Example
PI = 3.14  # correct

# 11. Avoid Trailing Semicolons
# Bad Example
z = 10;  # wrong

# Good Example
z = 10  # correct

# End of style guide