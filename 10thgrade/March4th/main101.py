import methods2 
import random 
'''
radius = int(input('Enter the radius of the circle: '))

answer = methods2.area_circle(radius)

print (answer)
'''
length = 100 
min = 1 
max = 50

new_list = methods2.random_lst(length, min, max)
print(new_list)

methods2.occuraces(new_list, 44)