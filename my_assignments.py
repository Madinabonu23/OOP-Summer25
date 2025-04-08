# create a variable for my name  
name = "Madinabonu Jaloldinova "
my_var = "Madinabonu Jaloldinova "

print(name)
print(my_var)

#  Assigning  a number to a variable 
x = 23
print(x)

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# Assigning a string to a variable
x = str("Learning Python is fun!")
print(x)

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# # If statement to check if b is greater than a 
a = 32 
b = 100 
if b > a :
    print("b is greater then a ")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") 


# Creating a list of fruits 
fruits = ["kiwi","cherry","apple","strawberry"]
print(fruits)

# Creating a list of cars
cars = ["Toyota", "Honda", "Ford", "BMW", "Mercedes"] 
print(cars) 

# Creating a list of students
students = ["Serra", "Sandugash", "Rayan", "Berke", "Sirri"] 
print(students) 

# Display each element of the 'fruits' list
print("Fruits:")
for fruit in fruits:
    print(fruits)

# Display each element of the 'cars' list
print("\nCars:")
for car in cars:
    print(car)

# Display each element of the 'students' list
print("\nStudents:")
for student in students:
    print(student)  

# Creating a dictionary to  student information
student = { 
   "name": "Nuray Mammadzade",
   "age": "23",
   "major": "Law"
}
print(student)

# Creating a dictionary to car information
car = {
    'brand': 'Toyota',
    'model': 'Camry',
    'year': 2021,
    'color': 'Blue'
}
print(car)

# Creating a dictionary to store horse information
horse = {
    'species': 'Equus caballus',
    'average_lifespan_years': 25,
    'weight_kg': 500,
    'height_cm': 150,
    'diet': 'Herbivore',
    'habitat': 'Grasslands and plains',
    'breeds': ['Arabian', 'Thoroughbred', 'Clydesdale', 'Appaloosa'],
}
print(horse)

# Creating Student class
class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Student("Nuray", 23)

print(p1.name)
print(p1.age)

# Creating Animal class 
class Animal:
    def __init__(self, name, species):
        self.name = name      
        self.species = species

p1 = Animal("Horse","Equus caballus" ) 

print(p1.name)
print(p1.species) 




















