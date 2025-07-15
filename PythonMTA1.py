# Open PythonMTA.pdf to view the choices of the answers.

# Question 1.
''' Evaluate the following Python arithmetic expression:
(3*(1+2)**2 - (2**2)*3) '''

''' Explanation: Values inside the parenthesis gets evaluated first, then exponents, then basic MDAS. '''

# first_step = 1+2
# second_step = 2**2
# third_step = first_step**2
# fourth_step = 3 * third_step
# fifth_step = second_step * 3
# answer = fourth_step - fifth_step

# print(answer)
# print((3*(1+2)**2 - (2**2)*3))

# Question 2.
''' Northwind Traders has hired you as an intern on the coding team that creates ecommerce applications. '''
''' You must write a script that asks the user for a value. The value must be used as a '''
''' whole number in a calculation, even if the user enters a decimal value. '''
''' You need to write the code to meet the requirements.  '''
''' Which code segment should you use? '''

''' Explanation: The user needs to input a value so create a variable first that asks for an input.
                 Then the problem specifies that it must be used as a whole number for calculation
                 so the data type should be an int. '''

# totalItems = int(input("How many Items would you like?"))

# Question 3.
''' You are creating a Python program that shows a congratulation message to employees on their service anniversary.
    You need to calculate the number of years of service and print a congratulatory message.
    You have written the following code. Line numbers are included for reference only.

      01 start = input(”How old were you on your start date?)
      02 end = input(’How old are you today?”)
      03

    You need to complete the program.
    Which code should you use at line 03? '''

''' Explanation: Before we can subtract the two variables, we need to first perform type casting on those variables.
                 We can change them to Int to perform subtraction. Then after that, transform them into strings to
                 perform string concatenation. '''

# start = input(”How old were you on your start date?)
# end = input(’How old are you today?”)
# print("Congratulations on " + str(int(end) - int(start)) + years of service!)

# Question 4.
''' You develop a Python application for your company. You want to add notes to your code
    so other team members will understand it. What should you do? '''

''' Explanation: Use # and type your note after the # '''

# Question 5.
''' You are writing an application that uses the sqrt function. The program must reference the function using
    the name squareRoot. You need to import the function. Which code segment should you use? '''

''' Explanation: We will import the math library and then import sqrt as squareRoot '''

# from math import sqrt as squareRoot

# Question 6.
''' This question requires that you evaluate the underlined text to determine if it is correct.
    You write the following code: '''

  # import sys
  # try:
  #   file_in = open(”in.txt”, ‘r’)
  #   file_out = open(”out.txt”, ‘w+’)

  # except lOError:
  #   print(’cannot open’, file_name)

  # else:
  #   i = 1
  #   for line in file_in:
  #   print(line. rstrip())
  #   file_out.write(”line “ + str(i) + “: “ + line)
  #   i = i + 1
  #   file_in.close()
  #   file_out.close ()

''' The out.txt file does not exist. You run the code. The code will execute without error.
    Review the underlined text. If it makes the statement correct, select “No change is
    needed.” If the statement is incorrect, select the answer choice that makes the statement
    correct. '''

''' Explanation: The correct answer is "No change is needed" because as stated in the problem, the code
                 will execute without error. '''

# Question 7.
''' You are writing a Python program to automate inventory. Your first task is to read a file
    of inventory transactions. The file contains sales from the previous day, including the
    item id, price, and quantity.
    The following shows a sample of data from the file:
    10, 200, 5
    20, 100, 1
    The code must meet the following requirements:
      . Each line of the file must be read and printed
      . If a blank line is encountered, it must be ignored
      . When all lines have been read, the file must be closed
  You create the following code. Line numbers are included for reference only:
  Which code should you write for line 05 and line 06?'''

# inventory = open(”inventory.txt”, ‘r’)
# eof = False

# while eof == False:
#   line = inventory.readline()
#   # BLANK
#     # BLANK
#       print(line)

# else:
#   print (“End of file”)
#   eof = True
#   inventory,close()

''' Explanation: The missing code in this code snippet are if line != '': and if line != "\n":
    In order for the code to read the whole txt file, it must ignore the blank line and the new line. '''

# Question 8.
''' Tailspin Toys uses Python to control its new toy Happy Clown. The program has errors
    that cause the clown to run around in an infinite circle. You have been hired to help
    debug the following Happy Clown code. Line numbers are included for reference only
    Which error exists in the code? '''

# import math
# #default motion for happy clown
# power = True
# move = 0

# while(power):
#   if move == 0:
#     turnValue = math.pi/move
#     move+=5

# else:
#   turnValue = 0
#   move = 0

''' Explanation: The error that will happen here is a run time error because line 7 divides by zero.
                 The code should've implemented an error handling code to avoid avoiding by zero. '''

# Question 9.
''' Woodgrove Bank is migrating their legacy bank transaction code to Python.
    You have been hired to document the migrated code.
    Which documentation syntax is correct? '''

''' Explanation: Below is the correct answer because it has the correct comment syntax and
                 the proper indentation. '''

# def get_balance():
    # Returns the current balance of the bank account
#   return

# Question 10.
''' You develop a Python application for your company. You need to accept input from the user
    and print that information to the user screen. You have started with the following code.
    Line numbers are included for reference only.
    Which code should you write at line 02? '''

# print ("What is your name?")
  # BLANK
# print(name)

''' Explanation: name = input() is the missing code. It follows the correct syntax of user input
                 where variable needs to be declared first then the input() function is used. '''
            







