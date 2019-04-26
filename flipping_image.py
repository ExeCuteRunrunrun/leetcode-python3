class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    #==============1======================================
        return [[1-a for a in reversed(arr)] for arr in A]
        # reversed(x) doesn't give a list, for information
        # pay attention to the [] logic, if we wanna return a list of list, should have 2 pairs of []
    #==============2=====================================
        # return [list(map(lambda x:1-x,list(reversed(i)))) for i in A]
