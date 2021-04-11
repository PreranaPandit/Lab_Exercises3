'''
Q.No.5 Write a function called show_stars(rows). If rows is 5,
it should print the following:
 *
 **
 ***
 ****
 *****

'''

for i in range (5):
    for j in range(i+1):
        print('*',end='')
    print('')

print( '\n')

for i in range (5,0,-1):
    for j in range(i-1):
        print('*',end='')
    print()