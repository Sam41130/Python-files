def is_palindrome(s):
    # Remove whitespace and convert to lowercase for a robust check
    cleaned_s = "".join(s.split()).lower()
    
    # Compare the string with its reverse
    return cleaned_s == cleaned_s[::-1]

# Test cases
print(is_palindrome("racecar"))  
print(is_palindrome("Hello"))   
print(is_palindrome("A man a plan a canal Panama")) 
