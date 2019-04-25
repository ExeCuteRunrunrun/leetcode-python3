class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
# =============1========================       
#         maybe = []
#         found_it = False
#         for i in range(len(A)/2+1):
#             if A[i] not in maybe:
#                 maybe.append(A[i])
                
#             else:
#                 return A[i]
#                 found_it = True
#         if not found_it:
#             return A[-1]

# ==============2======================
        maybe=[]
        for i in range(len(A)):
            if A[i] not in maybe:
                maybe.append(A[i])
                
            else:
                return A[i]
                break
