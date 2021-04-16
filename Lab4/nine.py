'''
9. Write a program to find the factorial of a number.
'''

def factorial(n):
    if n<0:
        return ':should be positive number'
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
#calling recursive function
num=int(input("enter the number to find factorial: "))
ans=factorial(num)
print(f"the factorial of {num} is {ans}")