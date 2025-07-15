# Question 11.
''' You develop a Python application for your school.
    You need to read and write data to a text file. If the file does not exist it must be created.
    If the file has content the content must be removed.
    Which code should you use? '''

''' Explanation: We will use the code below because it allows us to create the file if it doesn't exist.
                 If we choose option A, the file won't be created and it won't remove the existing contents
                 of the file. '''
            
# open("local_data", "w+")

# Question 12.
''' You evaluate the following code:
    numList = [0,1,2,3,4]
    print(5 in numList)
    What is the output of the print statement? '''

''' Explanation: The answer will be False because 5 doesn't exist in the list numList.
                 The in keyword checks if a value exists within a list or any data set.
                 '''

# Question 13.
''' A classmate has asked you to debug the code below. '''
''' What is the output that is printed to the screen? '''

''' Explanation: x = 4 so while x is greater or equal than 1, the while loop will continue. Then, the loop checks 
                 many conditions. So the first iteration, x = 4 and it satisfies t he first condition so it prints
                 party then x will be subtracted - 1 so it will now become 3. Then next, it goes through the loop again
                 but no condition satisfies it so it prints out birthday. x is now equal to 2. After that, it doesn't 
                 satisfy any condition again so it prints out birthday again. x is now equal to 1. Lastly, it satisfies
                 a condition where x - 2 < 0 so it prints out cake. The final output is party, birthday, birthday, cake '''

# x = 4
# while x >= 1:
#   if x % 4 == 0:
#     print (“party”)
#   elif x - 2 < 0:
#     print(”cake”)
#   elif x / 3 == 0:
#     print(”greeting”)
#   else:
#     print(”birthday”)
#   x = x - 1

# Question 14.
''' You write the code below. You run the code. What is the output value? '''

''' Explanation: When you multiply a list, it just repeats the elements in the list. If you want to multiply a number to a list
                 to get a product, you need to loop inside the list then multiply it. The correct answer is [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]''' 

# list_1 = [1, 2]
# list_2 = [3, 4]
# list_3 = list_1 + list_2
# list_4 = list_

# Question 15.
''' You are writing a Python application for a dance studio. The studio wants to encourage youth and seniors to sign up. 
    Minors and seniors must receive a 10% discount. 
    You write the following code. Line numbers are included for reference only. '''

''' Explanation: The missing code in the code block is if not (minor and senior): because only minors and seniors will get
                 a discount and others don't. '''

# def get_discount(minor, senior):
#   discount = .1
    # BLANK
#     discount = 0
#   return discount

# Question 16.
''' You develop a Python application for your school. A list named colors contains 200 colors. You need to slice the list 
    to display every other color starting with the second color.
    Which code should you use? '''

''' Explanation: We will use colors [1::2] to start from index one or in this case, color number 2 and then, use 2 to display
                 every other color. '''

                 
