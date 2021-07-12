print("hello world")

# this is a comment

name = "warren"
last_name = "christian"

print(name + " " + last_name)

full_name = name.capitalize() + " " + last_name.capitalize()

print(full_name)

print(full_name)

name_one = input("type your first name here" + " ")
name_two = input("type your last name here" + " ")

print(name_one.capitalize() + " " + name_two.capitalize())

# Custom string formatting
output = 'Hello, {0} {1}'.format(name, last_name)
print(output)
#f string
#An fstring is able to call a variable by name rather than array
fstring_example = f'Hello, {name} {last_name}'
print(fstring_example)

# Numeric Data Types

pi = 3.1415

first_num = 5
second_num = 2

print(first_num + second_num)
print(first_num ** second_num) # '**' is an exponent operator

# combining a string and a number in python causes issues
# here's how to do it

days_in_feb = 28
print(str(days_in_feb) + ' days in february')
# This converts the integer into a string by using the str() function
# storing a number as a string causes issues too
# the input() function always outputs a string

int_input_one = input('input the first number')
int_input_two = input('input the second number')
print(int(int_input_one) + int(int_input_two))
# int will obviously output a whole number
print(float(int_input_one) + float(int_input_two))
# float will output a decimal


