

 
# print-subString 
def printSubStr(string, low, high):
     
    for i in range(low, high + 1):
        print(string[i], end = "")
 
# This function prints :
# 1- longest palindrome subString
# 2- returns the length of the longest palindrome
#---------------------------------------------------------------------
def longestPalSubstr(string):
     
    # Get length of input String (string)
    n = len(string)
     
    # All subStrings of length 1
    # are palindromes
    maxLength = 1
    start = 0
     
    # Nested loop
    for i in range(n):
        for j in range(i, n):
            flag = 1
             
            # Check palindrome
            for k in range(0, ((j - i) // 2) + 1):
                if (string[i + k] != string[j - k]):
                    flag = 0
 
            # Palindrome
            if (flag != 0 and (j - i + 1) > maxLength):
                start = i
                maxLength = j - i + 1
                 
    print("Longest palindrome subString is: ", end = "")
    printSubStr(string, start, start + maxLength - 1)
 
    # Return length of LPS
    return maxLength
 
# Driver Code
if __name__ == '__main__':
 
    string = "abbac"
     
    print("\nLength is: ", longestPalSubstr(string))
