class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 :

            return s 

        rows = [""] * numRows

        pointRow = 0 

        directionUp = False

        for c in s : 
            
            rows[pointRow] += c

            if pointRow == 0 or pointRow == numRows - 1 :

                directionUp = not directionUp

            if directionUp :

                pointRow += 1 

            else : pointRow -= 1  

        return "".join(rows)
        
        