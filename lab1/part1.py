import math
import re

def task1_1():
    print("Task 1.1")
    input_check = False
    while not input_check:
        try:
            a, b = int(input("Enter number 1: ")), int(input("Enter number 2: "))
            input_check = True
            if a < 2 or b < 2:
                print("Numbers must be >= 2. Try again")
                input_check = False
            elif a >= b:
                print("Number 1 must be less than number 2. Try again")
                input_check = False
        except ValueError as error:
            print(error)

    primes = []

    if a <= 2 <= b:
        primes.append(2)
    
    start = max(a, 3)
    if start % 2 == 0:
        start += 1

    end = b
    if end % 2 == 0:
        end -= 1

    for i in range(start, end + 1, 2):
        i_sqrt = int(round(math.sqrt(i)))
        is_prime = True
        for j in range(3, i_sqrt + 1, 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    print(primes)

def task1_2():
    print("Task 1.2")
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'}
    res = []
    consonants_num = 0
    text = input("Enter text: ")
    words = re.split(r'[.,!?()\[\]|/\\\s]+', text)
    words = [word for word in words if word]
    for word in words:
        for letter in word:
            letter_low = letter.lower()
            if letter_low in vowels:
                res.append(letter)
            elif letter_low in consonants:
                consonants_num += 1
    print(f"- Word count: {len(words)}\n- Vowels count: {len(res)}\n- Consonants count: {consonants_num}")
    if len(res) == consonants_num != 0:
        print(f"- Vowels: {res}")

def task1_3():
    print("Task 1.3")
    numbers_str = input().split()
    numbers = [int(number) for number in numbers_str]
    unique_numbers = []
    pairs_counter = 0
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
            number_count = numbers.count(number)
            if number_count > 1:
                pairs_counter += ((number_count - 1) * number_count) / 2
    print(int(pairs_counter))

def task1_4():
    print("Task 1.4")
    sequence = input()
    result_dict = {}

    for char in sequence:
        digit = int(char)
        if digit in result_dict:
            result_dict[digit] += 1
        else:
            result_dict[digit] = 1

    print(result_dict)

def task1_5():
    print("Task 1.5")
    auto_parts = {
        "part A": ["descr A", 10, 10],
        "part B": ["descr B", 20, 20],
        "part C": ["descr C", 30, 30],
        "part D": ["descr D", 40, 40],
        "part E": ["descr E", 50, 50],
    }
    exit_flag = False
    while not exit_flag:
        print("-" * 36)
        action = int(input("Menu:\n - 1. View descriptions\n - 2. View prices\n - 3. View amount\n - 4. View al info\n - 5. Buy\n - 6. Leave\n Choose option: "))
        if not 1 <= action <= 6:
            print("Wrong input. Try again")
            continue
        match action:
            case 1:
                view_parts_descriptions(auto_parts=auto_parts)
            case 2:
                view_parts_prices(auto_parts=auto_parts)
            case 3:
                view_parts_amount(auto_parts=auto_parts)
            case 4:
                view_parts_full_info(auto_parts=auto_parts)
            case 5:
               auto_parts = buy_parts(auto_parts=auto_parts)
            case 6:
                exit_flag = True
        
def view_parts_descriptions(auto_parts):
    for name, info in auto_parts.items():
        print(f"{name} -- {info[0]}")

def view_parts_prices(auto_parts):
    for name, info in auto_parts.items():
        print(f"{name} -- {info[1]}")

def view_parts_amount(auto_parts):
    for name, info in auto_parts.items():
        print(f"{name} -- {info[2]}")

def view_parts_full_info(auto_parts):
    print(f"{'Name':^20}{'Description':^30}{'Price':^5}{'Amount':^8}")
    for name, info in auto_parts.items():
        print(f"{name:^20}{info[0]:^30}{info[1]:^5}{info[2]:^8}")

def buy_parts(auto_parts):
    parts_to_buy = {}
    parts_buy_exit_flag = False
    while not parts_buy_exit_flag:
        name = input("Enter name of the position: ")
        if not name in auto_parts:
            if name == 'n':
                parts_buy_exit_flag = True
            else: 
                print("There is no such position. Try again")
            continue
        if name not in parts_to_buy:
            parts_to_buy[name] = [0, 0]
        item = auto_parts.get(name)
        parts_to_buy[name][1] = item[2]
        amount = int(input("Enter amount of items: "))
        if amount > item[2]:
            print("There are not that many items. We'll count all of them")
        amount = min(amount, item[2])
        parts_to_buy[name][0] += amount
        item[2] -= amount
    total_cost = 0
    print(f"{'Name':^20}{'Amount':^6}{'For all':^10}")
    for name, item in parts_to_buy.items():
        cost = item[0] * item[1]
        total_cost += cost
        print(f"{name:^20}{item[0]:^6}{cost:^10}")
    print("-" * 36)
    print(f"{'Total':^20}{total_cost:^16}")
    return auto_parts
          
def task1_6():
    print("\nTask 1.6")
    numbers_str = input().split()
    numbers = [int(number) for number in numbers_str]
    numbers = tuple(numbers)
    for i in range(len(numbers)):
        if numbers[i] < 0:
            print(f"Index of the 1st negative number: {i}")
            break