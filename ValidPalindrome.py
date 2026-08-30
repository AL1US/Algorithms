class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_list = [char.lower() for char in s if char.isalnum()]

        left = 0
        right = len(cleaned_list) - 1
        
        while left < right:
            if cleaned_list[left] == cleaned_list[right]:
                left += 1
                right -= 1
                
            else:
                return False
            
        return True
    