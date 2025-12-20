from country import Country

class Countries_manager:
    def __init__(self):
        self.__countries = []

    def add_country(self, name, capital, area, population):
        self.__countries.append(Country(name, capital, area, population))

    def show_countries(self):
        print("-" * 80)
        print(f"{'Name':^25}{'Capital':^25}{'Area (km^2)':^15}{'Population':^15}")
        print("-" * 80)
        for country in self.__countries:
            print(f"{country.name:^25}{country.capital:^25}{country.area:^15}{country.population:^15}")
        print("-" * 80)
        print()

    def get_countries_by_area(self, min_area, max_area):
        result = [c for c in self.__countries if min_area <= c.area <= max_area]
        return result
    
    def get_countries_by_population(self, min_population, max_population):
        result = [c for c in self.__countries if min_population <= c.area <= max_population]
        return result