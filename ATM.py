allowedUser = ['Femi', 'Yemisi']
allowedPassword = ['FemiPass', 'YemiPass']

name = input("Enter your username: \n")
userId = allowedUser.index(name)


if(name in allowedUser):
    password = input("Enter your password: \n")
    
    if(password == allowedPassword[userId]):
        print("Welcome %s" %name)
        print("These are the available options")
        print("1. WIthdrawal")
        print("2. Cash deposit")
        print("3. Complaint")

        selectedOption = int(input("Please select an option: \n"))
        if(selectedOption == 1):
            print("You selected option %s" %selectedOption)
            amount = int(input("How much do you want to withdraw? \n"))
            print("Here is your audio %s" %amount)
            pass
        elif(selectedOption == 2):
            print("You selected option %s" %selectedOption)
            pass
        elif(selectedOption == 3):
            print("You selected option %s" %selectedOption)
            pass
        else:
            print("Invalid option selected, please try again")
        

    else:
        print("Incorrect password, please try again")

else:
    print("Name not found, please try again")
