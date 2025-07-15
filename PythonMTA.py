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

              
