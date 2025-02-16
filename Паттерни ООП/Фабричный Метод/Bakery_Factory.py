from enum import Enum


class BunsType (Enum):

    CINNAMON = 0,
    POPPY_SEED = 1,
    CHEESE = 2,
    STRAWBERRY_FILLING = 3,


class Buns:

    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price


class CinamonBuns (Buns):
    def __init__(self):
        super().__init__(15.0)


class PoppySeedBuns (Buns):
    def __init__(self):
        super().__init__(25.5)


class CheeseBuns (Buns):
    def __init__(self):
        super().__init__(25.8)


class BunsWithStrawberryFilling (Buns):
    def __init__(self):
        super().__init__(35.5)


def create_buns(bunstype: BunsType):
    buns_dict = {
        BunsType.CINNAMON: CinamonBuns, BunsType.CHEESE: CheeseBuns,
        BunsType.STRAWBERRY_FILLING: BunsWithStrawberryFilling,
        BunsType.POPPY_SEED: PoppySeedBuns
    }
    return buns_dict[bunstype]()


if __name__ == '__main__':
    for buns in BunsType:
        my_buns = create_buns(buns)
        print(f'Buns type: {buns}, price: {my_buns.get_price()}')
