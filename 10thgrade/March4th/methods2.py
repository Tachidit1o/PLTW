import math 
import random 
#Area of a circle
def area_circle(radius):
    area = math.pi * radius**2
    return print ('Your area for a circle with a radius of:  ',radius, 'is ', area, '.')

#Creating a random list: 
def random_lst (length, min, max):
    return [random.randint(min, max) for all in range(length)]

def occuraces(lst, target):
    count = 0 
    for num in lst: 
        if num == target: 
            count += 1
            return print(count)

