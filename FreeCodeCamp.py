def python_introduction():
    print("--- 1-5 ---")
    character_name = "Name"
    character_age = "35.5"
    is_male = True

    print("sentence " + character_name)
    print("sentence " + character_age)

    character_name = "Replace"
    print("sentence " + character_name)
    print("sentence " + character_age)

    a = 1
    b = 2
    c = a + b
    print(c)

    str1 = "code"
    str2 = "test"

    string = str1 + str2

    print(string)

    print(is_male)


def working_with_strings():
    # 6. Working With Strings
    print("--- 6 ---")
    phrase = "Giraffe Academy"
    print("1. " + phrase + " any word")
    print("2. Giraffe\nAcademy")
    print("3. \"Giraffe\" Academy")
    print("4. " + phrase.lower())
    print(phrase.isupper())
    print(len(phrase))
    print("7. " + phrase[0])
    print(phrase.index("f"))
    try:
        print(phrase.index("Acid"))
    except Exception as error:
        print(error)

    print(phrase.replace("Giraffe", "Elephant"))
    print(phrase.replace("affect", "phan"))


from math import *
def working_with_numbers():
    # 7. Working With Numbers
    print("--- 7 ---")
    print(2, 2.098, -2, 3 * 10)
    print(3 * 4 + 5)
    print(3 * (4 + 5))

    x = 5
    print(x)
    print("the number " + str(x))
    print(max(2, 2.06, -2, 3 * 10))
    value = [2, 2.06, -2, 3 * 10]
    print(max(value))

    print(floor(3.7))

def getting_input_from_users():
    # 8. Getting Input From Users
    print("--- 8 ---")
    name = input("Enter your name: ")
    print("Your name is: " + name)

def building_a_basic_calculator():
    # 9. Building a Basic Calculator
    print("--- 9 ---")
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    result1 = int(num1) + int(num2)
    print(result1)

    result2 = float(num1) + float(num2)
    print(result2)

def mad_libs_game():
    # 10. Mad Libs Game
    print("--- 10 ---")
    print("Roses are red")
    print("Violets are blue")
    print("I love you")

    color = input("Color: ")
    noun = input("Noun: ")
    celebrity = input("Celebrity: ")

    print("Roses are " + color)
    print(noun + " are blue")
    print("I love " + celebrity)


def lists():
    # 11. Lists
    print("--- 11 ---")
    letters = ["A", "B", "C", "D", "E"]

    print("0 = " + letters[0])
    print("-2 = " + letters[-2])
    print(f"1: = {letters[1:]}")
    print(f"1:3 = {letters[1:3]}")

    letters[3] = "X"
    print(f"[3] = {letters}")

    sub = letters[1:4]
    print(f"sub[2] = {sub} {sub[2]}")


def list_functions():
    # 12. List Functions
    print("--- 12 ---")
    letters = ["A", "B", "C", "D", "E"]
    numbers = ["1", "2", "3", "4", "5"]

    letters.extend(numbers)
    print(letters)

    letters.append("X")
    print(letters)

    numbers.insert(1, "0")
    print(numbers)
    numbers.remove("0")
    print(numbers)
    numbers.clear()
    print(numbers)

    unknown = list()
    unknown.append("A1")
    print(unknown)
    unknown.append("A2")
    unknown.append("A3")
    unknown.append("A4")
    unknown.append("A4")
    print(unknown)
    print(unknown.index("A4"))
    print(unknown.count("A4"))

    known = unknown.copy()
    known.reverse()
    print(known)


def tuples():
    # 13. Tuples
    print("--- 13 ---")
    coordinates = (4, 5)
    print(coordinates[1])

    coordinates = [(4, 5), (10, 20), (80, 100)]
    print(coordinates[1])


def functions():
    # 14. Functions
    print("--- 14 ---")
    def function_parameters(letter, number):
        print(letter + " " + number)


    function_parameters("A", "1")


def return_statements():
    # 15. Return Statement
    print("--- 15 ---")
    def function_cube_num(num):
        return num*num*num


    print(function_cube_num(3))


def if_statements():
    # 16. If Statements
    print("--- 16 ---")
    letter = input("Enter a letter: ")
    if letter == "a":
        print("The letter is a")
    elif letter == "b":
        print("The letter is b")
    else:
        if letter == "c":
            print("The letter is c")
        else:
            print("The letter is not a, b, c")


def if_statements_and_comparisons():
    # 17. If Statements & Comparisons
    print("--- 17 ---")
    def max_num(num1, num2, num3):
        if num1 >= num2 and num1 >= num3:
            return num1
        elif num2 >= num1 and num2 >= num3:
            return num2
        else:
            return num3

    print(max_num(6, 40, 3))


def building_a_better_calculator():
    # 18. Building a better Calculator
    print("--- 18 ---")
    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*" or op == "x":
        print(num1 * num2)
    else:
        print("Invalid operator")


def dictionaries():
    # 19. Dictionaries
    print("--- 19 ---")
    monthconversions = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        0: "May",
        1: "June",
        2: "July"
    }

    print(monthconversions["Apr"])
    print(monthconversions.get("Jan"))
    print(monthconversions.get("Dec"))
    print(monthconversions.get("Dec", "Not valid"))
    print(monthconversions[0])
    print(monthconversions.get(2))


def while_loop():
    # 20. While Loop
    print("--- 20 ---")
    i = 1
    while i <= 10:
        print(i)
        i += 1

    print("Done")


def building_a_guessing_game():
    # 21. Building a Guessing Game
    print("--- 21 ---")
    word = "giraffe"
    guess = ""
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != word and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input("Guess the word: ")
            guess_count += 1
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("Out of guesses. You Lose !")
    else:
        print("You got it !")


def for_loops():
    # 22. For Loops
    print("--- 22 ---")
    # iterate for each letter in the string
    for letter in "Giraffe Academy":
        print(letter)

    # iterate for each element in the collection
    letters = ["a", "b", "c", "d"]
    for each in letters:
        print(each)

    # iterate on range or starting range, excluding limit
    for index in range(10):
        print(index)

    for index in range(5, 10):
        print(index)

    for index in range(5):
        if index == 0:
            print("First index")
        else:
            print(index)


def exponent_function():
    # 23. Exponent Function
    print("--- 23 ---")
    def raise_power(base, power):
        result = 1
        for index in range(power):
            result = result * base
        return result


    num1 = 2
    num2 = 3

    print(raise_power(num1, num2))
    print(num1**num2)


def lists_and_nested_loops():
    # 24. 2D Lists & Nested Loops
    print("--- 24 ---")
    number_grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0]
    ]

    print(number_grid[0])
    print(number_grid[0][1])

    for row in number_grid:
        for col in row:
            print(col)


def building_a_translator():
    # 25. Building a Translator
    print("--- 25 ---")
    def translate(phrase):
        translation = ""
        for letter in phrase:
            if letter in "AEIOUaeiou":
                translation = translation + "*"
            else:
                translation = translation + letter
        return translation


    test = "quick brown fox"
    print(translate(test))


def comments():
    # 26. Comments
    print("--- 26 ---")
    # this is a comment
    '''
    multi line comment
    '''


def try_except():
    # 27. Try / Except
    print("--- 27 ---")
    try:
        number = int(input("Enter a number: "))
        print(number / 0)
    except ValueError:
        print("Invalid value entered")
    except ZeroDivisionError as err:
        print(err)


def reading_files():
    # 28. Reading Files
    print("--- 28 ---")
    employee_file = open("employees.txt", "r")

    print(employee_file.readlines()[1])
    print(employee_file.readlines())
    print(employee_file.readline())
    print(employee_file.readable())
    print(employee_file.read())

    employee_file.close()


def writing_to_files():
    # 29. Writing to Files
    print("--- 29 ---")
    employee_file = open("employees.txt", "a")

    employee_file.write("Kelly - Accountant\n")

    employee_file.close()


def modules_and_pip():
    # 30. Modules & Pip
    print("--- 30 ---")
    # tools.py is a separate python file with written code
    # all other modules are found at External Libraries > Lib
    import tools

    print(tools.roll_dice(3))

    # i.e. prompt> pip --version
    # pip install python-docx
    # External Libraries > Lib > site-packages


from student import ClassStudent
def classes_and_objects():
    # 31. Classes & Objects
    print("--- 31 ---")
    classstudentinstance1 = ClassStudent("Jim", "Business", 3.1, False)
    classstudentinstance2 = ClassStudent("Tom", "Economics", 2.5, True)

    print(classstudentinstance1.a)
    print(classstudentinstance2.a)

    classstudentinstance1.prints()


def building_a_multiple_choice_quiz():
    # 32. Building a Multiple Choice Quiz
    print("--- 32 ---")
    from question import QuestionAnswer
    question_prompts = [
        "Question 1: 1+1 =\na.2 b.3 c.4\nANSWER: ",
        "\nQuestion 2: 2*2 = \na.2 b.3 c.4\nANSWER: ",
        "\nQuestion 3: 3 / 3 = \na.3 b.1 c.6\nANSWER: "
    ]

    answer_key = [
        QuestionAnswer(question_prompts[0], "a"),
        QuestionAnswer(question_prompts[1], "c"),
        QuestionAnswer(question_prompts[2], "b"),
    ]


    def run_test(answer_key):
        score = 0
        for each in answer_key:
            answer = input(each.prompt)
            if answer == each.answer:
                score += 1
        print(str("\nYour score is: " + str(score)))


    run_test(answer_key)


def object_functions():
    # 33. Object Functions
    print("--- 33 ---")

    student1 = ClassStudent("Jim", "Business", 3.1, False)
    student2 = ClassStudent("Bryan", "Arts", 3.8, False)

    print("is " + student1.name() + " an honor student: " + str(student1.honor()))
    print("is " + student2.name() + " an honor student: " + str(student2.honor()))


def inheritance():
    # 34. Inheritance
    print("--- 34 ---")
    from ChefFile import ChefClass
    from ChineseChefFile import ChineseChefClass

    mychef = ChefClass()
    mychef.chicken()
    mychef.salad()
    mychef.special()
    print("-----------")

    mychef = ChineseChefClass()
    mychef.chicken()
    mychef.salad()
    mychef.special()
    mychef.fried()


def python_interpreter():
    # 35. Python Interpreter
    print("--- 35 ---")

    import time
    from datetime import timedelta

    time1 = time.process_time()

    time2 = time.process_time() - time1

    print(time1)
    print(timedelta(seconds=time2))


    letterslist = {
        "a": "apple",
        "b": "bus",
        "c": "cat",
        "d": "dog"
    }

    print(letterslist["a"])

import source.noclassimport
import source.importonly
from source.fromimport import ClassFromImport

def usingotherfiles():
    value1 = source.noclassimport
    print(value1.defnoclassimport_value())

    value2 = source.importonly.ClassImportOnly
    print(value2.defimportonly_value())

    value3 = ClassFromImport
    print(value3.deffromimport_value())


# -- pycharm > alt+7 --
# python_introduction()
# working_with_strings()
working_with_numbers()
# getting_input_from_users()
# building_a_basic_calculator()
# mad_libs_game()
# lists()
# list_functions()
# tuples()
# functions()
# return_statements()
# if_statements()
# if_statements_and_comparisons()
# building_a_better_calculator()
# dictionaries()
# while_loop()
# building_a_guessing_game()
# for_loops()
# exponent_function()
# lists_and_nested_loops()
# building_a_translator()
# comments()
# try_except()
# reading_files()
# writing_to_files()
# modules_and_pip()
# classes_and_objects()
# building_a_multiple_choice_quiz()
# object_functions()
# inheritance()
# python_interpreter()
# usingotherfiles()