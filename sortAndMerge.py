"""
You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order. 
"""

def sorting(a,b):
    curA=len(a)-len(b)-1
    curB =len(b)-1
    curT=len(a)-1
    
    
    while curB>=0:
        if curA>=0 and a[curA]>b[curB]:
            a[curT],a[curA]=a[curA],a[curT]
            curA -=1
        else:
            a[curT]=b[curB]
            curB -=1
            
        
        curT -=1
    
def main ():
    a=[1,3,5,7,8,None,None,None]
    b=[0,4,10]
    
    sorting(a, b)
    print a


main()