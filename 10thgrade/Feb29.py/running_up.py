import turtle 
import methods
'''
turtle.Turtle()
turtle.fd(100)

question = input('How old are you?')
print (methods.age(question))

calculation = int(input(('What is the raduis of your cirle? ')))
print(methods.area(calculation))
'''
'''
int_list = [1, 2, 6, 4, 2, 5, 2, 6, 2]
print (int_list)
question2 = int(input('What number would you like to count in the list?'))
print(methods.occurances(int_list, question2 ))
'''
length = 100
min = 0 
max = 50
crazy_list = methods.random_list(length, min, max)
print(crazy_list)


question2 = int(input('What number would you like to count in the list?'))
print(methods.occurances(crazy_list, question2 ))
'''
turtle.Screen()

turtle.mainloop()
'''