import random

class Dice:
    __sides = 6

    @property
    def sides(self):
        return self.__sides

    def __init__(self, color):
        self.__color = color
        self.__last_roll = 0

    @property
    def color(self):
        return self.__color
    
    @property
    def last_roll(self):
        return self.__last_roll

    # метод экземпляра класса
    def roll(self):
        result = random.randint(1, self.__sides)
        self.__last_roll = result
        return result
    
    # метод класса
    @classmethod
    def change_sides(cls, num):
        if 2 < num < 13:
            cls.__sides = num
            return True
        else:
            return False
    
    # статический метод
    @staticmethod
    def print_rules():
        print("+ RULES:\n- Single 1 = 100\n- Single 5 = 50\n- Three 1s = 300\n- Three 2s = 200\n- Three 3s = 300\n- Three 4s = 400\n- Three 5s = 500\n- Three 6s = 6")
        