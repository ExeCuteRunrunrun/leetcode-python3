class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ranger = list(range(len(S)+1))   # ranger = [0,1,2...,N] N=len(S)+1

        A = []
        for i in range(len(S)):
            if S[i]=="I":
                A.append(ranger.pop(0))  # start from the minimal if "I"
            elif S[i]=="D":
                A.append(ranger.pop())   # start from the maximul if "D"
        A.append(ranger.pop())           # end with the last integer in ranger
        return A
