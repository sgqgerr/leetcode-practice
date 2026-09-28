class Solution:
    def myAtoi(self, s: str) -> int:

        if len(s) == 0: 

            return 0

        i = 0 

        sign = 1 

        result = 0 

        while i < len(s) and s[i] == " " : i += 1 

        if i < len(s) and s[i] == "-" : 
            sign = -1  
            i += 1 

        elif i < len(s) and s[i] == "+" : i += 1

        while i < len(s) and s[i].isdigit() == True : 
            result = result * 10 + int(s[i]) 
            i += 1

        result = result * sign

        if result < -2**31 : return -2**31 
        elif result > 2**31 - 1 : return 2**31 - 1  
        else : return result  