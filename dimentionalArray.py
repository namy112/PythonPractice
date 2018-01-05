"""
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.

Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

"""

def generateMatrix(noOfRows,noOfColums): 
    
    matrix=[]
    for columnCell in range (noOfColums):
        
        row=[]
        for rowCell in range(noOfRows):
            value=rowCell*columnCell
            row.append(value)
            
        matrix.append(row)  
            
    print(matrix)

def main():

    noOfRows=input("Enter no of rows")
    noOfColums=input("Enter no of coloums")

    if noOfColums >0 and noOfRows>0:
       generateMatrix(noOfRows, noOfColums)
    else:
        print ("Try again! Please enter a positive number")
             
main()
