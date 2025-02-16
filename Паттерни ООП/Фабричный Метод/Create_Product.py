from abc import ABC, abstractmethod
from Product import Pizza, Donuts, Pies, Water


class Create(ABC):


    def сocking(self):

        return "The pizza will be ready in 30 minutes."

class CreateProduct(Create):


    def cocking(self, сhoice):
        if сhoice == "pizza":
            prodact = Pizza()
            print(prodact.stuffing())
            asq=input('Хотите воды?, Введите да или нет')
            if asq.lower() =='да':
                water = Water()
                print (water.stuffing("orang"))
            else:
                print ("Ok")

        elif сhoice == 'donat':
            prodact=Donuts()
            print(prodact.stuffing())

        elif сhoice == 'pie':
            prodact = Pies()
            print(prodact.stuffing())

        elif сhoice == 'вода':
            water = Water()
            print (water.stuffing("апельсином"))

        else:
            print("Извините у нас такого нет")


salesman = CreateProduct()
product = (input('Выберите выпечку Pizza, Donut, Pie. Может воды с апельсином'))
salesman.cocking(product.lower())
#
