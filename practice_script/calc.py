# imports

# global vars


# functions
def print_menu(): 
    separator= "------------"
    print(separator)
    print("Calc 3000")
    print(separator)
    print("[1] Sum two numbers")
    print("[2] Subtract two numbers")
    print("[3] Multiply two numbers")
    print("[4] Divide two numbers")


# plain instructions
print_menu()
opt = input("Please select an option: ")
    # ask the user for num1, num2, and print the results of adding those numbers
num1 = float(input("Select a number: "))
num2= float(input("Select a second number: "))

if opt == "1": 
    result = num1 + num2
    print("The result is: " + str(result))

elif opt == "2":
    result = num1 - num2
    print("The result is: " + str(result))


elif opt == "3":
    result = num1 * num2
    print("The result is: " + str(result))

# division,
# if the second number is zero, show an error
# else divide and show the result

# This is as close as I could get without the terminal crashing. I still can't get the error msg to appear or the result :)
elif opt == "4":   
    if opt == "4" and num2 == "0":
        print("Second number cannot be 0, Please select another number: ")
    
elif opt == "4":
    if opt == "4" and num2 >= "1":
        result = num1 // num2
        print("The result is: " + str(result))
    