"""
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
"""
n= input("Please enter a number..")

def generateWorks(n):
    for number in range(1,n+1):
        if number%7==0:
            yield number
        
for i in generateWorks(n):
    print(i)