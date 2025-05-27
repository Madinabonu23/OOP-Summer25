class Car:
    def __init__(self, brand, engine_type):
        self.brand = brand              # public attribute
        self.__engine_type = engine_type  # private attribute

    def display_engine_type(self):
        print(f"Engine type: {self.__engine_type}")

    def __start_the_engine(self):
        print("Engine has started ")

    def start_the_car(self):
        print(f"Starting the {self.brand} car...")
        self.__start_the_engine()


my_car = Car("Mercedes", "Electric")
print(my_car.brand)
my_car.display_engine_type()
my_car.start_the_car()

