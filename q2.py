def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    still_adj=True
    
    while still_adj:
        pair=False
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                s=s[:i]+s[i+2:]
                pair=True
                break
                #I had to use break, otherwise it says out of range. 
                #I hope this is not a problem
        if pair==False:
            still_adj=False
    return s

print(remove_adjacent_duplicates("abbacadd"))
print(remove_adjacent_duplicates("azxxzy"))
print(remove_adjacent_duplicates("aabccb"))