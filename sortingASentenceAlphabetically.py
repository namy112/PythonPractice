"""
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


TestCase1='without,hello,bag,world'
TestCase2=''
TestCase3='hello,hello,hello,Hello'

def sortingAString(a):
        
    splitString=a.split(',')
    sortsplitString=sorted(splitString)
    joinString=','.join(sortsplitString)
    print(joinString)
    
sortingAString(TestCase1)
sortingAString(TestCase2)
sortingAString(TestCase3)