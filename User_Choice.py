def User_Choice():
    print("Welcome To Rock-Paper-Scissors Game!".center(60,"-"))
    valid_choices = ["rock" , "paper" ,"scissors"]
    while(True):
        choice = input("Which move do you choice?||(choices : [rock,paper,scissors]):")
        if(choice.lower() in valid_choices):
            break
        else:
            print("Please enter a valid move!")
            print()
            continue
    return choice.lower()
