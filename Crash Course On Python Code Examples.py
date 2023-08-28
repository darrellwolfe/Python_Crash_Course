#Examples

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)
    
#Examples

for i in range(10):
  print("Hello, World!")

#Calculations 

print(4+5)

print(9*7)

print(-1/4)

print(1/3)

print(((2050/5)-32)/9)

print(2**10)

print(((1+2)*3)/4)

ratio = (1+(5**(1/2)))/2
print(ratio)

print((6-2)/(5*(1+4))+3)

# Variables

base = 5
height = 3
area = (base*height)/2

print(area)


print("a "+ "Apple "+ "Snapple")


bill = 47.28 # Assign "bill" variable with bill amount
tip = bill * .15 # Multiply by stated tip rate 
total = bill + tip # Sum the "total" of the "bill" and "tip"
share = total/2 # Divide "total" by number of friends dining
print("Each person needs to pay: " + str(share)) # Enter the required string and "share" 
# Hint: Remember to convert incompatible data types



numerator = 10
denominator = 1
result = numerator / denominator
print(result)

#Not quite. Remember that we are dividing two numbers, and
#need to end up with the answer of 1.

numerator = 10
denominator = 10
result = numerator / denominator
print(result)
#So conditonal could be added "if 0, replace with numerator column"

print("How "+"do "+"you "+"like "+"Python"+"so "+"far?")

word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"
print(word1+" "+word2+" "+word3+" "+word4+" "+word5+" "+word6+" "+word7)



# Creating Functions

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

# Do not indent any of the following lines of code as they are 
# meant to be located outside of the function above

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the my_trip_km conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result of
#    my_trip_km. Fill in the blank to print the result.
print("The round-trip in kilometers is " + str(my_trip_km*2))




# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
___, ___ = order_numbers(100, 99)
print(smaller, bigger)


smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

Widgy, Wodgy = order_numbers(100, 99)
print(Widgy, Wodgy)  # Output would be 99, 100






#Define print_seconds

def print_seconds(hours, minutes, seconds):
    print(hours*3600+minutes*60+seconds)


print_seconds(1,2,3)
#output will print to the screen


print(10>1)

print("cat"=="dog")

print("cat"!="dog")



def is_even(number):
  if number % 2 == 0
    return True
  else
    return False
  
# else can be left out in this case for a reason I don't understand. 
def is_even(number):
  if number % 2 == 0
    return True
    return False

See Notion

def hint_username(username):
  if len(username) < 3:
    print("Invalid username. Must be > 3 but < 15")
  elif len(username) > 15:
    print("Invalid username. Must be > 3 but < 15")
  else:
    print("Valid username")

username = "JosephineMagnaliousTheThird"
username = "Jo"
username = "Joseph123"
hint_username(username)


if condition1:
    action1
elif condition2:
    action2
else:
    action3



# The value of 10*4 (40) is greater than 14+23 (37), therefore this 
# comparison expression will return the Boolean value of True.


print(10*4 > 14+23) # Should print True

# The letter "t" has a Unicode value of 116 and the letter "s" has a
# Unicode value of 115. Since 116 is not less than 115, the 
# comparison of "tall" < "short" (or 116 < 115) is False. 

print("tall" < "short")  # Should print False







# This function accepts one variable as a parameter
def translate_error_code(error_code):
 
# The if-elif-else block assesses the value of the variable
# passed to the function as a parameter. The if statement uses 
# the equality operator == to test the value of the variable.
# This test returns a Boolean (True/False) result.
    if error_code == "401 Unauthorized":
# If the comparison above returns True, then the indented 
# line(s) inside the if-statement will run. In this case, the
# action is to assign a string to the translation variable.
# The remainder of the if-elif-else block will not run.
# The Python interpreter will skip to the next line outside of 
# the if-elif-else block. In this case, the next line is the 
# return value statement.  
        translation = "Server received an unauthenticated request"
 
# If the initial if-statement returns a False result, then the
# first elif-statement will run a different test on the value
# of the variable.
    elif error_code == "404 Not Found":
# If the first elif-statement returns a True result, then the
# indented line(s) inside the first elif-statement will run. 
# After this line, the remainder of the if-elif-else block will
# not run. The Python interpreter will skip to the next line
# outside of the if-elif-else block. 
        translation = "Requested web page not found on server"
 
# If both the initial if-statement and the first elif-statement 
# return a False result, then the second elif-statement will
# run.
    elif error_code == "408 Request Timeout":
# If the second elif-statement returns a True result, then the
# indented line(s) inside the second elif-statement will run. 
# After this line, the remainder of the if-elif-else block will
# not run. The Python interpreter will skip to the next line
# outside of the if-elif-else block. 
        translation = "Server request to close unused connection"
 
# If the conditional tests above do not produce a True result
# then the else-statement will run. 
    else:
        translation = "Unknown error code"
# The if-elif-else block ends.

# The next line outside of the if-elif-else block will run
# after exiting the block. In this case, the next line returns
# the output from the if-elif-else block.
    return translation

# The print() function allows us to display the output of the
# function. To call a function in a print statement, the syntax
# is print(name_of_function(parameter))
print(translate_error_code("404 Not Found"))

# Expected output:
# Requested web page not found on server












# Sets value of the "number" variable
number = 25

# The "number" variable will first be compared to 5. Since it is 
# False that "number" is not less than or equal to 5, the expression indented 
# under this line will be ignored. 
if number <= 5: 
   print("The number is 5 or smaller.")
 
# Next, the "number" variable will be compared to 33. Since it is 
# False that "number" is equal to 33, the expression indented under 
# this line will be ignored. 
elif number == 33:
   print("The number is 33.")
 
# Then, the "number" variable will be compared to 32 and 6. Since it 
# is True that 25 is less than 32 and greater than 6, the Python 
# interpreter will print "The number is less than 32 and/or greater
# than 6." Then, it will exit the if-elif-else statement and the remainder 
# of the if-elif-else statement will be ignored.
elif number < 32 and number >= 6:
   print("The number is less than 32 and greater than 6.")
 
else:
   print("The number is " + str(number))
 
# Expected output is: 
# The number is less than 32 and greater than 6.







# This function rounds a variable number up to the nearest 10x value
def round_up(number):
  x = 10
# The floor division operator will calculate the integer value of
# "number" divided by x: 35 // 10 will return the integer 3.
  whole_number = number // x
# The modulo operator will calculate the remainder value of "number"
# divided by x: 35 % 10 will return the remainder value 5.
  remainder = number % x
# If the remainder is greater than 0: 
  if remainder >= 5: 
# Return x multiplied by the (whole_number+1) to round up
    return x*(whole_number+1)
# Else, return x multiplied by the whole_number to round down
  return x*whole_number
 
# Calls the function with the parameter value of 35.
print(round_up(35)) # Should print 40




def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))





if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)

number = 10







def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = ___
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = ___
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return ___
    return ___

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192



def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    return filesize

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192



name = ___
home_address = ___
print(name + " lives at her home address of " + home_address)
# Should print "Marjery lives at her home address of 1234 Mockingbird Lane"


def clothing_type(temp):
    if ___:
        clothing = "T-Shirt"
    elif ___:
        clothing = "Sweatshirt"
    elif ___:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing


print(clothing_type(72)) # Should print T-Shirt
print(clothing_type(55)) # Should print Sweatshirt
print(clothing_type(65)) # Should print Sweatshirt
print(clothing_type(50)) # Should print Jacket
print(clothing_type(45)) # Should print Jacket
print(clothing_type(32)) # Should print Heavy Coat
print(clothing_type(0)) # Should print Heavy Coat




def clothing_type(temp):
    if temp > 65:
        clothing = "T-Shirt"
    elif temp > 50 and temp <= 65:
        clothing = "Sweatshirt"
    elif temp > 32 and temp <= 50:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing


print(clothing_type(72)) # Should print T-Shirt
print(clothing_type(55)) # Should print Sweatshirt
print(clothing_type(65)) # Should print Sweatshirt
print(clothing_type(50)) # Should print Jacket
print(clothing_type(45)) # Should print Jacket
print(clothing_type(32)) # Should print Heavy Coat
print(clothing_type(0)) # Should print Heavy Coat




test_num = 12
if test_num > 15:
    print(test_num / 4)
else:
    print(test_num + 3)





def complementary_color(color):
    if ___ == "blue":
        complement = "orange"
    elif ___ == "yellow":
        complement = "purple"
    elif ___ == "red":
        complement = "green"
    ___:
        complement = "unknown"
    return ___

print(complementary_color("blue")) # Should print orange
print(complementary_color("yellow")) # Should print purple
print(complementary_color("red")) # Should print green
print(complementary_color("black")) # Should print unknown
print(complementary_color("Blue")) # Should print unknown
print(complementary_color("")) # Should print unknown



def complementary_color(color):
    if color == "blue":
        complement = "orange"
    elif color == "yellow":
        complement = "purple"
    elif color == "red":
        complement = "green"
    else:
        complement = "unknown"
    return complementary_color

print(complementary_color("blue")) # Should print orange
print(complementary_color("yellow")) # Should print purple
print(complementary_color("red")) # Should print green
print(complementary_color("black")) # Should print unknown
print(complementary_color("Blue")) # Should print unknown
print(complementary_color("")) # Should print unknown



def sum(x, y):
        return(x+y)
print(sum(sum(1,2), sum(3,4)))





def make_positive(number):
    if number < __:
        result = ___ * -1 
    else:
        result = __
    return result


print(make_positive(-4))   # Should print 4
print(make_positive(0))    # Should print 0
print(make_positive(-.25)) # Should print 0.25
print(make_positive(5))    # Should print 5




def make_positive(number):
    if number < 0:
        result = number * -1 
    else:
        result = number
    return result


print(make_positive(-4))   # Should print 4
print(make_positive(0))    # Should print 0
print(make_positive(-.25)) # Should print 0.25
print(make_positive(5))    # Should print 5


There's a small mistake in your code. You're returning the function name `complementary_color` instead of the variable `complement` that holds the calculated complementary color. Here's the corrected version of your code:

```python
def complementary_color(color):
    if color == "blue":
        complement = "orange"
    elif color == "yellow":
        complement = "purple"
    elif color == "red":
        complement = "green"
    else:
        complement = "unknown"
    return complement

print(complementary_color("blue"))   # Should print orange
print(complementary_color("yellow")) # Should print purple
print(complementary_color("red"))    # Should print green
print(complementary_color("black"))  # Should print unknown
print(complementary_color("Blue"))   # Should print unknown
print(complementary_color(""))       # Should print unknown
```

Now, the corrected code will properly return the calculated complementary color instead of the function name.


def difference(x, y):
    z = x - y
    return z


print(difference(5, 3))



x = 5*2
((10 != x) or (10>x))


def safe_division(numerator, denominator):
    # Complete the if block to catch any "denominator" variables
    # that are equal to 0.
    if denominator == 0:
        result = 0
    else:
        # Complete the division equation.
        result = numerator/denominator
    return result


print(safe_division(5, 5)) # Should print 1.0
print(safe_division(5, 4)) # Should print 1.25
print(safe_division(5, 0)) # Should print 0
print(safe_division(0, 5)) # Should print 0.0



x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))



def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)


def count_down(start_number):
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)



