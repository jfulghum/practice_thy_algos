def longestPalindromicSubstring(string):
    
    if not string or len(string) == 1:
        return string
    
    max_palindrome = ''
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            s = string[i:j+1]
            rev_s = s[::-1]
            
            if s == rev_s:
                max_palindrome = max(max_palindrome, s, key=len)
                
    return max_palindrome
