import math
class Solution:
    # Question Difficulty: Easy     
    # Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward. Try not to convert the integer to a string.
    #     
    # Examples:     
    #     
    # 121 is a palendrome, returns true         
    # -121 not a palendrome, returns false
    
    # this function's purpose is to find out whether or not a number is a palindrome
    # parameters: an integer
    # returns: a boolean value (True or False)     
    def isPalindrome(self, x: int) -> bool:
        # checks if number is negative, if it is it will never be a palindrome         
        if(x < 0):
            return False
        # if number is between 0 and 10 (right side exclusive). If it is, it will return true        
        elif(x < 10):
            return True
        # number of digits in x      
        num_of_digits = int(math.log10(x))+1
        # a pointer starting on the last number          
        backwards_pointer = num_of_digits -1
        # a pointer starting on the first number         
        forwards_pointer = 0
        
        # if pointers are not equal (middle number), or the first pointer is not greater than the last pointer
        # (the pointers passed eachother) then loop         
        while(forwards_pointer != backwards_pointer and not forwards_pointer > backwards_pointer):
            left_digit = self.get_digit(x, forwards_pointer)
            right_digit = self.get_digit(x, backwards_pointer)
            
            # if the digits in each place are equal, move forward pointers, else number is not a palindrome           
            if(left_digit == right_digit):
                forwards_pointer = forwards_pointer + 1
                backwards_pointer = backwards_pointer - 1
            else:
                return False
        
        return True
    # this functions purpose is to get the digit at a speicific place of a number.
    # parameters:
    #   number = integer number
    #   n = the place that you want to find a number at 
    # returns: integer     
    def get_digit(self,number, n):
        return number // 10**n % 10