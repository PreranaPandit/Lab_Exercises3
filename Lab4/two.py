'''
2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
  C = (5/9) * (F - 32)
'''

f=float(input("enter the value in fahrenheit degree:"))
c=(5/9)*(f-32)
print(c)
print(f"the value of {f} degree fahrenheit is {c} degree celcius")


c=int(input("enter the value in celcius degree:"))
f=(1.8*c)+32
print(f)
print(f"the value of {f} degree celcius is {c} degree fahrenheit")