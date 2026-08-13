import random
choices = ["rock" , "paper" , "scissors"]
def Computer_Choice(data):
    random_int = random.randint(0,2)
    choice = data[random_int]
    return choice
