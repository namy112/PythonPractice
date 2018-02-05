
def checkPermutationUsigDict(inputStr1,inputStr2):
    
    if len(inputStr1)!= len(inputStr2):
        print("This is not a permutation of a string")
    dict1={}
    dict2={}
    
    for letter in inputStr1.lower():
        if letter not in dict1:
            dict1[letter]=1
        else:
            dict1[letter]+=1
    
    for letter in inputStr2.lower():
        if letter not in dict2:
            dict2[letter]=1
        else:
            dict2[letter]+=1
    
    print(dict1)
    print(dict2)
    
    print(dict1==dict2)
    
checkPermutationUsigDict('india', 'Indai')

def checkPermutation(inputStr1,inputStr2):
    
    if len(inputStr1)!= len(inputStr2):
        print("This is not a permutation of a string")
        
    sortedInputStr1=sort(inputStr1)
    sortedInputStr2=sort(inputStr2)
    
    if inputStr1==inputStr2:
        print("Its permutation")
        
checkPermutationUsigDict('india', 'indai')
    
    