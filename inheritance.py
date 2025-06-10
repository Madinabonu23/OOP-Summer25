# %% [markdown]
# ## Inheritance 

# %% [markdown]
# ## A parent class 

# %%
class Animal:
    def give_sound(self,sound):
        print(sound)

my_animal = Animal()
my_animal.give_sound("Meow")

# %% [markdown]
# ## Child class 

# %%
class Cat(Animal):
    def meow(self):
        self.give_sound("Meow")


my_cat = Cat()
my_cat.meow()

# %% [markdown]
# ## A parent class 

# %%
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name 

# %% [markdown]
# ## A child class 

# %%
## student class without inheritance 
class Student:
    def __init__(self, first_name, last_name, index_number):
        self.first_name = first_name
        self.last_name = last_name
        self.index_number = index_number 

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}, index: {self.index_number}")


student1 = Student('Madinabonu', 'Jaloldinova', '35485')

student1.display_info()

# %% [markdown]
# ## Student class with inheritance (as child class )

# %%
class Student(Person):
    def __init__(self, first_name, last_name, index_number):
        super().__init__(first_name, last_name)
        self.index_number = index_number 

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}, index: {self.index_number}")


student1 = Student('Madinabonu', 'Jaloldinova', '35485')

student1.display_info()


