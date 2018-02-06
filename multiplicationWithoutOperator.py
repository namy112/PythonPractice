

def multWithNoOp(number,multiplyer):
    
   
    multiplyerP=abs(multiplyer)
    numberP=abs(number)
    count=0        
    for i in range(multiplyerP):
        count += numberP
    
    if number > 0 and multiplyer > 0:
        print (count)
    elif number <0 and multiplyer <0 :
        print(count)
    else:
        print(-count)
    


multWithNoOp(2, 6)
multWithNoOp(2, -6)
multWithNoOp(-2, 6)
multWithNoOp(-2, -6)
multWithNoOp(2, 0)
multWithNoOp(0, 0)
multWithNoOp(0, 2)