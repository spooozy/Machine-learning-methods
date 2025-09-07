from example import Example
from countries_manager import Countries_manager
from stationery import Pen, Pencil, Handle
from dice import Dice

def task3_1():
    example = Example(5, 2)
    example.create_local_var()
    example.sum_global_vars()
    example.pow_dynamic_vars()

def task3_2():
    c_manager = Countries_manager()
    c_manager = create_countries(c_manager)
    c_manager.show_countries()
    try:
        filter_num = int(input("- 1. Filter by area\n- 2. Filter by population\n--- Choose filter: "))
        match filter_num:
            case 1:
                min_area = int(input("Enter min area: "))
                max_area = int(input("Enter max area:" ))
                result = c_manager.get_countries_by_area(min_area, max_area)
                show_results(result)
            case 2:
                min_population = int(input("Enter min population: "))
                max_population = int(input("Enter max population:" ))
                result = c_manager.get_countries_by_population(min_population, max_population)
                show_results(result)
            case _:
                print("Next time choose another option")
    except ValueError as e:
        print(e)
    
def create_countries(c_manager):
    c_manager.add_country("The North 🐺", "Winterfell", 3500030, 2190073)
    c_manager.add_country("Marley 💣", "Liberio", 3100086, 35004371)
    c_manager.add_country("Nilfgaard 🌞", "Nilfgaard City", 2200190, 14719205)
    c_manager.add_country("Earth Kingdom 🐉", "Ba Sing Se", 4508900, 68000912)
    c_manager.add_country("Durmstrang Territory 🦅", "Durmstrang Castle", 180000, 8000)
    c_manager.add_country("Narnia 🦁", "Cair Paravel", 947801, 367997)
    return c_manager

def show_results(result):
    print("-" * 80)
    print(f"{'Name':^25}{'Capital':^25}{'Area (km^2)':^15}{'Population':^15}")
    print("-" * 80)
    for country in result:
        print(f"{country.name:^25}{country.capital:^25}{country.area:^15}{country.population:^15}")
    print("-" * 80)
    print()

def task3_3():
    pen = Pen("La Modernista Diamonds")
    pencil = Pencil("Slingshot-Pencil")
    handle = Handle("PONY")
    pen.draw()
    pencil.draw()
    handle.draw()

def task3_4():
    dice1 = Dice("green")
    dice2 = Dice("blue")
    Dice.print_rules()
    print("-" * 25)
    print(f"{'Dice':^6}|{'Sides':^7}|{'Last Roll':^12}")
    print("-" * 25)
    dice2.roll()
    print(f"{'Dice1':^6}|{dice1.sides:^7}|{dice1.last_roll:^12}")
    print(f"{'Dice2':^6}|{dice2.sides:^7}|{dice2.last_roll:^12}")
    print("-" * 25)
    dice1.change_sides(4)
    print(f"{'Dice1':^6}|{dice1.sides:^7}|{dice1.last_roll:^12}")
    print(f"{'Dice2':^6}|{dice2.sides:^7}|{dice2.last_roll:^12}")
    print("-" * 25)
    dice1.roll()
    print(f"{'Dice1':^6}|{dice1.sides:^7}|{dice1.last_roll:^12}")
    print(f"{'Dice2':^6}|{dice2.sides:^7}|{dice2.last_roll:^12}")
    print("-" * 25)
    Dice.change_sides(3)
    print(f"{'Dice1':^6}|{dice1.sides:^7}|{dice1.last_roll:^12}")
    print(f"{'Dice2':^6}|{dice2.sides:^7}|{dice2.last_roll:^12}")
    print("-" * 25)
    