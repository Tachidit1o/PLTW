import math
import random

def circumference(radius):
    area = math.pi * radius**2
    return print('The area of a circle with the radius of', radius, 'is: ', area, '.')

def random_list(length, min, max):
    return [random.randint(min, max) for balboni in range(length)]

def occurences(lst, target):
    count = 0 
    for num in lst: 
        if num == target: 
            count += 1 
    return count