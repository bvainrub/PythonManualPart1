
def isPalindrome(x):
    string_input = str(x)
    reverse_string = ""
    for i in  string_input:  
        reverse_string = i + reverse_string
    if reverse_string == string_input:
        return True
    else:
        return False

 

strin_new= isPalindrome(-121)
print(strin_new)


def isPalindrome(x):
    original_string = str(x)
    reversed_string = original_string[::-1]
        
    if original_string == reversed_string:
        return True
    else:
        return False

strin_new = isPalindrome(-121)
print(strin_new)








#reversed_string = original_string[::-1]