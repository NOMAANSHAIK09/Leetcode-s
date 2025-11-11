# Q)Given an integer x, return true if x is a palindrome, and false otherwise.
#try 
#x = int(input("enter the integer to check: "))

#class Solution:
 #   def isPalindrome(self, x):
  #      s = str(x)  # convert to string
 #       if s == s[::-1]:
  #          print("true")
  #      else:
  #          print("false")

#obj = Solution()
#obj.isPalindrome(x)

# correct one 

class Solution:
    def isPalindrome(self, x):
        s = str(x)
        return s == s[::-1]
