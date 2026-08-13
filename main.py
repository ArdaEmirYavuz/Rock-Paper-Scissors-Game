import ComputerChoice as computer
import UserChoice as user
computer_choice = computer.Computer_Choice(computer.choices)
user_choice = user.User_Choice()
paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
if(computer_choice == "rock" and user_choice == "paper"):
    print("-".center(50,"-"))
    print("You chose:\n{}".format(paper))
    print("Computer chose:\n{}".format(rock))
    print("Congrats! You won!")
    print("-".center(50,"-"))
elif(computer_choice == "scissors" and user_choice == "rock"):
    print("-".center(50,"-"))
    print("You chose:\n{}".format(rock))
    print("Computer chose:\n{}".format(scissors))
    print("Congrats! You won!")
    print("-".center(50,"-"))
elif(computer_choice == "paper" and user_choice == "scissors"):
    print("-".center(50,"-"))
    print("You chose:\n{}".format(scissors))
    print("Computer chose:\n{}".format(paper))
    print("Congrats! You won!")
    print("-".center(50,"-"))
elif(computer_choice == user_choice):
    if(computer_choice == "rock"):
        print("-".center(50,"-"))
        print("You chose:\n{}".format(rock))
        print("Computer chose:\n{}".format(rock))
        print("Its a draw!")
        print("-".center(50,"-"))
    elif(computer_choice == "scissors"):
            print("-".center(50,"-"))
            print("You chose:\n{}".format(scissors))
            print("Computer chose:\n{}".format(scissors))
            print("Its a draw!")
            print("-".center(50,"-"))
    elif(computer_choice == "paper"):
                print("-".center(50,"-"))
                print("You chose:\n{}".format(paper))
                print("Computer chose:\n{}".format(paper))
                print("Its a draw!")
                print("-".center(50,"-"))
else:
    if(computer_choice == "rock"):
        computer_choice ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
    elif(computer_choice == "paper"):
        computer_choice="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
    elif(computer_choice == "scissors"):
        computer_choice = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    if(user_choice == "rock"):
            user_choice ="""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
"""
    elif(user_choice == "paper"):
            user_choice="""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
"""
    elif(user_choice == "scissors"):
            user_choice = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
"""
    print("-".center(50,"-"))
    print("You chose:\n{}".format(user_choice))
    print("Computer chose:\n{}".format(computer_choice))
    print("Unfortunately you beaten...")
    print("-".center(50,"-"))
