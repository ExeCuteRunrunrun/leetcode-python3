########################
# again, the discription is not so obvious for the first look;
# actually, instead of saying array A = ["abcdef","uvwxyz"]
# we should perhaps say array A but in table form like: 
# ["abcdef",
#  "uvwxyz"]
# then it's more clear to understand what "column" stands for

################### 1. slow ####################
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        columns = []
        for col in zip(*A): # col = ("c","d","g")
            columns.append(list(col))
        # all possible values in D are in range(len("cbd"))
        D = set()
        for d in range(len(columns)):
            col = columns[d]
            for i in range(1,len(col)):
                if col[i]<col[i-1]:
                    D.add(d)
        return len(D)
        
################# 2. little better ####################     
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        D = set()
        zipped = list(zip(*A))
        for d in range(len(zipped)): # col = ("c","d","g")
            col = zipped[d]
            for i in range(1,len(col)):
                if col[i]<col[i-1]:
                    D.add(d)
        return len(D)
    
