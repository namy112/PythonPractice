"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""


testcase1='hello world! 123'

stringList=[]
for alphabet in testcase1:
    stringList.append(alphabet)
    
noOfDigits=0
noOfAlphabets=0
for element in stringList:
    if element.isalpha()==True:
        noOfAlphabets+=1
    elif element.isdigit()==True:
        noOfDigits+=1
    else:
        pass
    
print("No of alphabets is :%s and digits :%s " %(noOfAlphabets,noOfDigits))