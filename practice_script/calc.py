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


elif opt == "4":
    result = num1 / num2
    print("The result is: " + str(result))

if opt == "0":
    print("Error: Please choose another number: ")
