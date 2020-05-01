class Solution:
    def lengthOfLongestSubstring(self, s: str):
        used_letters = {}
        number_of_letters = 0
        max_letters = 0
        
        
        for letter in s:
            

            


            if letter in used_letters:
                number_of_letters = 0
                used_letters = {}
            else:
                number_of_letters = number_of_letters + 1
                used_letters[letter] = True
            
            if(number_of_letters > max_letters):
                max_letters = number_of_letters
    
        return max_letters

    
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))