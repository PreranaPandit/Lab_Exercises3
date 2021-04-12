'''
Q.No.9 Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same
 backward as forward, e.g., madam or nurses run.
'''

def palindrome():
    string=input("Enter the the string: ")
    rev_string=string[::-1]
    if string==rev_string:
        return "this is palindrome"
    else:
        return "this is not palindrome"

print(palindrome())
