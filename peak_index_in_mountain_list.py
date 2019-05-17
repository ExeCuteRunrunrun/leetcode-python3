class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        maxim = max(A)
        return A.index(maxim)
