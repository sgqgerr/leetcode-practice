class Solution:

    PHONE = {
        2 : ["a", "b", "c"],
        3 : ["d", "e", "f"],
        4 : ["g", "h", "i"],
        5 : ["j", "k", "l"],
        6 : ["m", "n", "o"],
        7 : ["p", "q", "r", "s"],
        8 : ["t", "u", "v"],
        9 : ["w", "x", "y", "z"]
    }

    def letterCombinations(self, digits: str) -> list[str]:
        
        result = [""]

        for digit in digits:
            new_result = []
            for combo in result:
                for letter in self.PHONE[int(digit)]:
                    new_result.append(combo + letter)
            result = new_result 
        return result 
        
        