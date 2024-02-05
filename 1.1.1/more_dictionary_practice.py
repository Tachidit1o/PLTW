whatever = {"land animal": "elephant",
            "water animal": "whale",
            "air animal": "humming bird",
            "space animal": "space cat"}

user_input = input('Hello, would you like a list of animals (yes or no)?')
if (user_input == 'yes'):
    all_whatever = len(whatever)
    
    for x,y  in whatever.items(): 
        print (x,y)

    second_question = input("Is there an animal type you would like to delete (yes or no)?")
    if (second_question == "yes"):
        while True: 
#Enter a while loop to avoid anything else that is not in the dictionary. 
            third_question =  input("What type of animal category would you like to delete (please enter the category name only, e.g. 'air animal')?")         
            if (third_question in whatever):
                del whatever[third_question]
                print( f" {third_question} has been deleted. ")

                for x, y in whatever.items():
                    print (x, y)    
                break        
            else: 
                print('You did not enter an existing category')
else: 
    print('Great, have a good day then...')

