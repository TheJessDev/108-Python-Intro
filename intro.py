
print("Hello World")

# this is a comment

# create variables
name = "Jess"
last_name = "Morrison"
age = 99
total = 1.33
found = False

print(name) 
print ("Morrison")
print(age)
print(total)
print(found)

# contact string
print(name + " " + last_name)

#math
print(1*2)
print(3+3)
print(10-3)
print(7/4)

# error
#print("name" + "3")
#print(name + 3 )

# conditional statements
if(age<100) : 
    print("don't worry!")
    #print("inside the if")
    #print("still in the if")
elif age==100:
    print("congrats!")
else:
    print("Sorry!")
print("I'm outside")


# functions
def say_hello():
    print("Hello there")
    print("From a function")

def say_hi(name):  # with paramaters
    print("Hi" + name)

def get_day():
    return "Monday"  # function can return values


# calling the function
say_hello()
say_hello()

say_hi("Jess")  #  give a value or use the value given

day = get_day()
print("today is " + day)



