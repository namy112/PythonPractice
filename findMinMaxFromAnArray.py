
#Given a array, output min and max element


tc1=[4,1,2,6,8,10]
tcNegativeValues=[-17,-1,0,-7,1]
tcEmptyArray=[]

def findMinMax(a):  
    if len(a)<1:
        print("DONT PASS AN EMPTY ARRAY")
        return
        
    min=a[0]
    max=a[0]
    for elem in a:
        if elem>max:
            max=elem
        if elem < min:
            min=elem
            
    print(min,max)
    

findMinMax(tcNegativeValues)
findMinMax(tcEmptyArray)