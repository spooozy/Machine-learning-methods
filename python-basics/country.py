class Country:
    def __init__(self, name, capital, area, population):
        self.__name = name
        self.__capital = capital
        self.__area = area
        self.__population = population
    
    @property
    def name(self):
        return self.__name

    @property
    def capital(self):
        return self.__capital
    
    @property
    def area(self):
        return self.__area
    
    @property
    def population(self):
        return self.__population
    
    def __repr__(self):
        return f"Country('{self.name}', '{self.capital}', {self.area}, {self.population})"
    
    
    
        
