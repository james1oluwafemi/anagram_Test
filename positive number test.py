user_no = input("Enter a number: \n")
try:
    user_no = float(user_no)
    print("Hooray, you entered a number")

    if user_no > 0:
        print("True")

    elif user_no == 0:
        print("Neutral")
    
    else:
        print("False")

except:
    print("User input is not a number. Please enter a number")  