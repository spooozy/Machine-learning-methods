import math
import re
import numpy as np
import random

def task2_1():
    num = int(input("Enter number: "))
    print(get_fact(num))

def get_fact(num):
    if num < 0:
        return 0
    if num == 0:
        return 1
    if num == 1 or num == 2:
        return num
    return fact_tree(2, num)
    
def fact_tree(l, r):
    if(l > r):
        return 1
    if (l == r):
        return l
    if (r - l == 1):
        return l * r
    m = int((l+r) / 2)
    return fact_tree(l, m) * fact_tree(m + 1, r)

def task2_2():
    test_data = {
        'list': [1, -2, 3, -4, 5, -2, 3, 1],
        'set': {"word1", "word2", "word3", "word4"},
        'number_int': 17, 
        'number_float': 15.0,
        'number_prime': 29,
        'number_not_prime': 9,
        'string': "Hello world programming",
        'string_empty': ""
    }
    for name, data in test_data.items():
        result = process_task2_2(data)
        print(f"- {name}: {data}")
        for key, value in result.items():
            print(f"-- {key}: {value}")

def process_task2_2(arg):
    # list
    if isinstance(arg, list):
        # find the sum of negative numbers
        negative_sum = sum(num for num in arg if isinstance(num, (int, float)) and num < 0)
        unique_items = []
        for item in arg:
            if item not in unique_items:
                unique_items.append(item)
        return {
            'type' : 'list',
            'negative_sum' : negative_sum,
            'unique_items': unique_items
        }
    # set
    elif isinstance(arg, set):
        return {
            'type' : 'set',
            'words_count': len(arg)
        }
    # number: int -> is prime?
    elif isinstance(arg, int):
        is_prime = False
        if arg <= 1:
            is_prime = False
        elif arg == 2:
            is_prime = True
        elif arg % 2 == 0:
            is_prime = False
        else:
            is_prime = True
            arg_sqrt = int(round(math.sqrt(arg)))
            for i in range(3, arg_sqrt + 1, 2):
                if arg % i == 0:
                    is_prime = False
                    break
        return {
            'type': 'integer',
            'is_prime': is_prime
        }
    elif isinstance(arg, float):
        return {
            'type': 'float',
            'is_prime': 'False'
        }
    elif isinstance(arg, str):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'}
        consonants_num = 0
        vowels_num = 0
        words = re.split(r'[.,!?()\[\]|/\\\s]+', arg)
        words = [word for word in words if word]
        if len(words) == 0:
            return {
                'result': 'empty line'
            }
        for word in words:
            for letter in word:
                letter = letter.lower()
                if letter in vowels:
                    vowels_num += 1
                elif letter in consonants:
                    consonants_num += 1
        max_word_len = max(words, key = len)
        return{
            'consonants_num': consonants_num,
            'vowels_num' : vowels_num,
            'max_word_len' : max_word_len
        }
    else:
        return {
            'type' : 'unknown'
        }

def task2_3():
    n = random.randint(1, 5)
    m = random.randint(1, 5)
    matrix = np.random.randint(-10, 10, (n, m))
    print(matrix)
    for line in matrix:
        result = any(num > 0 for num in line)
        if not result:
            print(f"Line without positive numbers: {line}")
            break
    matrix = matrix * (-1)
    print(f"Each line contains a positive number\n {matrix}")

def task2_4():
    print()
    secret_number = random.randint(1,20)
    attempts = 3
    attempt = 1
    loser_flag = False
    try:
        while attempt <= attempts:
            print(f"- Attempt {attempt}/{attempts}")
            try:
                guess = int(input("- Enter number: "))
                if guess == secret_number:
                    print("- Ok, fine, you're  right.")
                    return
                if guess > secret_number:
                    print("- The secret number is even smaller than your chanses of winning")
                    attempt += 1
                else:
                    print("- The secret number is as far from you as the moon is")
                    attempt += 1
                print()
            except ValueError:
                if not loser_flag:
                    print("- Are you stupid? You need to enter a number\n- I forgive you for the first time\n")
                    loser_flag = True
                else:
                    attempt +=1
                    print("- I warned you. -1 attempt\n")
                
        raise Exception("Attempts are over")
    except Exception as e:
        if "Attempts are over" in str(e):
            print(f"- You are definitaly stupid\n- I thought of a number {secret_number}")
        else:
            print("- Unforeseen error\n- Either you are clumsy or I am stupid\n- I am inclined to the first option.")
    finally:
        print("\n--- GAME OVER ---\n")