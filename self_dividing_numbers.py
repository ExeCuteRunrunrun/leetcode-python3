class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        out = []
        for i in range(left, right+1):
            can = True
            for digit in str(i):
                if (int(digit) == 0):
                    can = False
                elif (i % int(digit) !=0):
                    can = False
            if can:
                out.append(i) 
        return out
