'''
Q.No.4 Write a function that returns the sum of multiples of 3 and 5 between 0 and
limit (parameter). For example, if limit is 20,
it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20
'''


def name (limit):
    sum=0
    for i in range (0,limit+1,1):
        if not i % 5 or not i % 3:
            sum = sum + i
    print(sum)

#function calling
a=int(input("Enter the number: "))
b=name(a)
print('End')




'''
a = int(input("enter a number: "))
n = 0
for i in range(0, a +1, 1):
     if not i % 5 or not i % 3:
         n = n + i
print(n)
'''