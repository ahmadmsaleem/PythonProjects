#This Python script prompts the user to input lower and upper bounds, and then asks for a guess within that range. 
#If the guess matches a randomly generated number, the user wins. 
#If not, they are prompted to try again until they guess correctly.
import random
def exists(variable):
    try:
        eval(variable)
    except NameError:
        return False
    return True
def is_number(variable):
    return isinstance(variable, (int, float))
while True:
    try:
        if not exists('lower'):
            lower = float(input("Enter Lower bound:- "))
            if not is_number(lower):
                print("Please enter a valid number.")

        if not exists('upper'):
            upper = float(input("Enter Upper bound:- "))
            if not is_number(upper):
                print("Please enter a valid number.")
            random_num = random.uniform(lower, upper)

        if not exists('choice'):
            guess = float(input("Enter a number:- "))
            if not is_number(guess):
                print("Please enter a valid number.")
            elif int(random_num) != int(guess):
                print("Wrong choice!")
            else:
                choice = guess
                print("YOU WON!")
                break
              
    except ValueError:
        print("Please enter a valid number.")
