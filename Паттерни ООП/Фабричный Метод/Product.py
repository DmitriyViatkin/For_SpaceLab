from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def stuffing(self):

        return 'Продукты для начинки: \
                Сыр моцарелла - 300 г, \
                Сыр твердый - 200 г\
                Помидоры - 2-3 шт.\
                Колбаса вареная - 200-250 г\
                Колбаса копченая\
                Грибы шампиньоны\
                Соус томатный'
    """def Cocking(self):

        return "Запекать 20 хв"""


class Pizza (Product):

    def __init__(self):
        self.name = "Pizza Napoletana"
        self.weight = "400g"
        self.price = 10
        self.stuffings= "помидоров и сыра моцарелла"
    def stuffing(self):

        return f"Вы выбрали {self.name} с начинкой  из {self.stuffings} \n \
        с вас {self.price}"


class Pies(Product):

    def __init__(self):
        self.name = "Пирог"
        self.weight = "400g"
        self.price = 8
        self.stuffings="Яблоки"

    def stuffing(self):

        return f"Вы выбрали {self.name} с начинкой  из {self.stuffings} \n \
        с вас {self.price}"


class Donuts(Product):
    def __init__(self):
        self.name = "Пончики"
        self.weight = "400g"
        self.price = 15
        self.stuffings = "сгущонкой"

    def stuffing(self):

       return f"Вы выбрали {self.name} с начинкой  из {self.stuffings} \n \
        с вас {self.price}"


class Water(Product):

    def stuffing(self, taste):
        return f"ваша вода с {taste}"
