import math
import random 

def age(age):
    print ('You are ', age, 'years old.')

def area(radius):
    result = math.pi * radius**2 
    print ('Your area of a circle is: ', result, '. ')

def occurances(list, target):
    count = 0 
    for num in list:
        if num == target: 
            count += 1
    return print('The number',target, 'shows up', count, 'times.')

def random_list(length, min, max):
    return [random.randint (min, max) for baloni in range(length)]

