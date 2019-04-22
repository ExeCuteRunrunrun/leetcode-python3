class Solution:
    # to find how many letters in string S (for stone) are letters in string J (for jewel)
    # input J, S
    # output n (number of common letters)
    def numJewelsInStones(self, J: str, S: str) -> int:
        n=0
        for i in S:
            if i in J:
                n+=1        
        return n
