# character_name = "Name"
# character_age = "35.5"
# is_male = True
#
# print("sentence " + character_name)
# print("sentence " + character_age)
#
# character_name = "Replace"
# print("sentence " + character_name)
# print("sentence " + character_age)
#
# a = 1
# b = 2
# c = a + b
# print(c)
#
# str1 = "code"
# str2 = "test"
#
# string = str1 + str2
#
# print(string)

# 6. Working With Strings
# phrase = "Giraffe Academy"
# print("1. " + phrase + " any word")
# print("2. Giraffe\nAcademy")
# print("3. \"Giraffe\" Academy")
# print("4. " + phrase.lower())
# print(phrase.isupper())
# print(len(phrase))
# print("7. " + phrase[0])
# print(phrase.index("f"))
# print(phrase.index("Acid"))
# print(phrase.replace("Giraffe", "Elephant"))
# print(phrase.replace("affect", "phan"))

# 7. Working With Numbers
# print(2, 2.098, -2, 3 * 10)
# print(3 * 4 + 5)
# print(3 * (4 + 5))
#
# x = 5
# print(x)
# print("the number " + str(x))
# print(max(2, 2.098, -2, 3 * 10))
#
# from math import *
#
# print(floor(3.7))

# 8. Getting Input From Users
# name = input("Enter your name: ")
# print("Your name is: " + name)

# 9. Building a Basic Calculator
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result1 = int(num1) + int(num2)
# print(result1)
#
# result2 = float(num1) + float(num2)
# print(result2)

# 10. Mad Libs Game
# print("Roses are red")
# print("Violets are blue")
# print("I love you")
#
# color = input("Color: ")
# noun = input("Noun: ")
# celebrity = input("Celebrity: ")
#
# print("Roses are " + color)
# print(noun + " are blue")
# print("I love " + celebrity)

# # 11. Lists
# letters = ["A", "B", "C", "D", "E"]
#
# print(letters[0])
# print(letters[-2])
# print(letters[1:])
# print(letters[1:3])
#
# letters[3] = "X"
# print(letters)
#
# sub = letters[1:4]
# print(sub[2])

# 12. List Functions
# letters = ["A", "B", "C", "D", "E"]
# numbers = ["1", "2", "3", "4", "5"]
#
# letters.extend(numbers)
# print(letters)
#
# letters.append("X")
# print(letters)
#
# numbers.insert(1, "0")
# print(numbers)
# numbers.remove("0")
# print(numbers)
# numbers.clear()
# print(numbers)
#
# unknown = []
# unknown.append("A1")
# print(unknown)
# unknown.append("A2")
# unknown.append("A3")
# unknown.append("A4")
# unknown.append("A4")
# print(unknown)
# print(unknown.index("A4"))
# print(unknown.count("A4"))
#
# known = unknown.copy()
# known.reverse()
# print(known)

# 13. Tuples
# coordinates = (4, 5)
# print(coordinates[1])
#
# coordinates = [(4, 5), (10, 20), (80, 100)]
# print(coordinates[1])

# 14. Functions
# def function_parameters(letter, number):
#     print(letter + " " + number)
#
#
# function_parameters("A", "1")

# 15. Return Statement
# def function_cube_num(num):
#     return num*num*num
#
#
# print(function_cube_num(3))

# 16. If Statements
# letter = input("Enter a letter: ")
# if letter == "a":
#     print("The letter is a")
# elif letter == "b":
#     print("The letter is b")
# else:
#     if letter == "c":
#         print("The letter is c")
#     else:
#         print("The letter is not a, b, c")

# 17. If Statements & Comparisons
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(6, 40, 3))

# 18. Building a better Calculator
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*" or op == "x":
#     print(num1 * num2)
# else:
#     print("Invalid operator")

# 19. Dictionaries
# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     0: "May",
#     1: "June",
#     2: "July"
# }
#
# print(monthConversions["Apr"])
# print(monthConversions.get("Jan"))
# print(monthConversions.get("Dec"))
# print(monthConversions.get("Dec", "Not valid"))
# print(monthConversions[0])
# print(monthConversions.get(2))

# 20. While Loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# print("Done")

# 21. Building a Guessing Game
# word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != word and not out_of_guesses:
#     if guess_count < guess_limit:
#         guess = input("Guess the word: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of guesses. You Lose !")
# else:
#     print("You got it !")

# 22. For Loops
# # iterate for each letter in the string
# for letter in "Giraffe Academy":
#     print(letter)
#
# # iterate for each element in the collection
# letters = ["a", "b", "c", "d"]
# for each in letters:
#     print(each)
#
# # iterate on range or starting range, excluding limit
# for index in range(10):
#     print(index)
#
# for index in range(5, 10):
#     print(index)
#
# for index in range(5):
#     if index == 0:
#         print("First index")
#     else:
#         print(index)

# 23. Exponent Function
# def raise_power(base, power):
#     result = 1
#     for index in range(power):
#         result = result * base
#     return result
#
#
# num1 = 2
# num2 = 3
#
# print(raise_power(num1, num2))
# print(num1**num2)

# 24. 2D Lists & Nested Loops
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
#
# print(number_grid[0])
# print(number_grid[0][1])
#
# for row in number_grid:
#     for col in row:
#         print(col)

# 25. Building a Translator
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             translation = translation + "*"
#         else:
#             translation = translation + letter
#     return translation
#
#
# test = "quick brown fox"
# print(translate(test))

# 26. Comments
# # this is a comment
# '''
# multi line comment
# '''

# 27. Try / Except
# try:
#     number = int(input("Enter a number: "))
#     print(number)
#     num = 10/0
# except ValueError:
#     print("Invalid")
# except ZeroDivisionError as err:
#     print(err)

# 28. Reading Files
# employee_file = open("employees.txt", "r")
#
# print(employee_file.readlines()[1])
# print(employee_file.readlines())
# print(employee_file.readline())
# print(employee_file.readable())
# print(employee_file.read())
#
# employee_file.close()

# 29. Writing to Files
# employee_file = open("employees.txt", "a")
#
# employee_file.write("Kelly - Accountant\n")
#
# employee_file.close()

# 30. Modules & Pip
# # tools.py is a separate python file with written code
# # all other modules are found at External Libraries > Lib
# import tools
#
# print(tools.roll_dice(3))
#
# # i.e. prompt> pip --version
# # pip install python-docx
# # External Libraries > Lib > site-packages

# 31. Classes & Objects
# from student import ClassStudent
# import student
#
# student1 = student.ClassStudent("Jim", "Business", 3.1, False)
#
# print(student1.a)
#
# student.ClassStudent.prints()

# 32. Building a Multiple Choice Quiz
# from question import QuestionAnswer
# question_prompts = [
#     "Question 1: \na. b. c.\nANSWER: ",
#     "\nQuestion 2: \na. b. c.\nANSWER: ",
#     "\nQuestion 3: \na. b. c.\nANSWER: "
# ]
#
# answer_key = [
#     QuestionAnswer(question_prompts[0], "a"),
#     QuestionAnswer(question_prompts[1], "c"),
#     QuestionAnswer(question_prompts[2], "b"),
# ]
#
#
# def run_test(answer_key):
#     score = 0
#     for each in answer_key:
#         answer = input(each.prompt)
#         if answer == each.answer:
#             score += 1
#     print(str("\nYour score is: " + str(score)))
#
#
# run_test(answer_key)

# 33. Object Functions
# from student import ClassStudent
# student1 = ClassStudent("Jim", "Business", 3.1, False)
# student2 = ClassStudent("Bryan", "Arts", 3.8, False)
#
# print(student2.honor())

# 34. Inheritance
# from ChefFile import ChefClass
# from ChineseChefFile import ChineseChefClass
#
# myChef = ChefClass()
# myChef.chicken()
# myChef.salad()
# myChef.special()
# print("-----------")
#
# myChef = ChineseChefClass()
# myChef.chicken()
# myChef.salad()
# myChef.special()
# myChef.fried()

# 35. Python Interpreter


# import time
# from datetime import timedelta
#
# time1 = time.process_time()
#
# time2 = time.process_time() - time1
#
# print(time1)
# print(timedelta(seconds=time2))


# lettersList = {
#     "a": "apple",
#     "b": "bus",
#     "c": "cat",
#     "d": "dog"
# }
#
# print(lettersList["a"])
