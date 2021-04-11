'''
Q.No.8 Write a Python function that takes a number as a parameter and
check the number is prime or not.
Note : A prime number (or a prime) is a natural number greater
than 1 and that has no positive divisors other than 1 and itself.
'''

def prime(n):
    if n%2==0 or n%3==0:
        return "It is not a prime number"
    else:
        return "It is a prime number"
a=int(input("Enter the number to check it is prime or not: "))
b=prime(a)
print(b)