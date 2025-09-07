import math

class Example:
    __static_var_1 = 10
    __static_var_2 = -2
    val = 10

    def __init__(self, val1 = 5, val2 = 5):
        self.dynamic_var_1 = val1
        self.dynamic_var_2 = val2

    def create_local_var(self):
        local_var = "Hi, I'm local variable"
        print(local_var)
    
    def sum_global_vars(self):
        print(f"Class variable 1: {self.__static_var_1}, Class variable 2: {self.__static_var_2}\n Sum = {Example.__static_var_1 + Example.__static_var_2}")

    def pow_dynamic_vars(self):
        print(f"Object variable 1: {self.dynamic_var_1}, Object variable 2: {self.dynamic_var_2}\n Pow 1^2 = {math.pow(self.dynamic_var_1, self.dynamic_var_2)}") 