def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    max_str=""
    potential_max=""
    
    for i in range(len(s)):
        for j in range(i+2, len(s)+1):
            potential_max=s[i:j]
            
            if potential_max == potential_max[::-1]:
                if len(potential_max)>len(max_str):
                    max_str=potential_max
                
                
    if len(max_str)>=2:
                
        return max_str
    else:
        return ""
    
print(longest_palindromic_substring("baabaad"))
print(longest_palindromic_substring("cbbd"))
print(longest_palindromic_substring("a"))