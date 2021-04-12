'''
Q.No.10 Write a program to find the factorial of a number using functions.
'''

#function definition
def factorial(num):
    fact=1
    # for loop for finding factorial
    for i in range(1, num+1):
        fact=fact*i
        # return factorial
    return fact

number=int(input("Please enter any number to find factorial: "))
#function call and assign the value to variable result
result=factorial(number)
print("The factorial of %d = %d"%(number,result))