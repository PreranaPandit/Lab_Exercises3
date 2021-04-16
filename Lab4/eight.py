'''
8. Write a Python program to get the Fibonacci series between 0 to 50.
    Note : The Fibonacci Sequence is the series
    of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
    Every next number is found by adding up the two numbers before it
'''

'''
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b
'''


fibo = [-1]
new_number = 1
while new_number < 50:
    '''
    The append() method in python adds a single item to the existing list. 
    It doesn’t return a new list of items but will modify the original 
    list by adding the item to the end of the list.
    '''
    fibo.append(new_number)
    new_number = fibo[-2] + fibo[-1]
    print(new_number)
