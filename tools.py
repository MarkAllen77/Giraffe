import random

feet_to_mile = 5280
meters_to_kilometer = 1000
letters = ["A", "B", "C", "D"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1]


def roll_dice(num):
    return random.randint(1, num)
