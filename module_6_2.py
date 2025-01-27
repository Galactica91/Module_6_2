class Vehicle:

    __COLOR_VARIANTS = ['White', 'Black', 'Yellow', 'Blue', 'Cyan', 'Red']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return print(f"Модель: {self.__model}")

    def get_horsepower(self):
        return print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        return (f"Цвет: {self.__color}")

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in Vehicle.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)

vehicle1 = Sedan('Joe Black', 'BMW Series 6', 'black', 500)

vehicle1.print_info()
print('----------------')
vehicle1.set_color('Pink')
vehicle1.set_color('BLUE')
vehicle1.owner = 'Jane Doe'
print('----------------')
vehicle1.print_info()
