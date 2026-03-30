def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    
    if a[0:2]=="0b":
        a=a[2:]
        
    if b[0:2]=="0b":
        b=b[2:]
    
    maxx=0
    
    if len(a)>=len(b):
        new_a=a
        new_b="0"*(len(a)-len(b))+b
        maxx=len(new_b)
    else:
        new_b=b
        new_a="0"*(len(b)-len(a))+a
        maxx=len(new_a)
    
            
    result=""
    carry=0
    
    for i in range(maxx-1,-1,-1):

        summ=carry
        
        if new_a[i]=="1":
            summ+=1
        if new_b[i]=="1":
            summ+=1
            
        result=str(summ%2)+result
        carry=summ//2
    if carry==1:
        result="1"+result
        
    while len(result)>1 and result[0]=="0":
        result=result[1:]
        
        
    return "0b"+result

print(add_binary("0b11", "0b1"))
print(add_binary("0b1010", "0b1011"))
print(add_binary("0b0", "0b0"))