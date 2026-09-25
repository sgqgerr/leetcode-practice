class Solution:
    def longestPalindrome(self, s: str) -> str:

        bestLeft = 0 

        bestRight = 0

        for i in range(len(s)):

            left = i 

            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:

                left = left - 1 

                right = right + 1

            left = left + 1 

            right = right - 1 

            if bestRight - bestLeft < right - left:

                bestLeft = left 

                bestRight = right
        
        for i in range(len(s)):

            left = i 

            right = i + 1 

            while left >= 0 and right < len(s) and s[left] == s[right]:

                left = left - 1 

                right = right + 1 

            left = left + 1 

            right = right - 1 

            if bestRight - bestLeft < right - left: 

                bestLeft = left

                bestRight = right

        return s[bestLeft:bestRight + 1] 

