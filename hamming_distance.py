class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        b_x = '{0:031b}'.format(x)
        b_y = '{0:031b}'.format(y)
        print(b_x, b_y)
        count = 0
        # as given condition: 0<x,y<2**31
        for i in range(31):
            if b_x[i]!=b_y[i]:
                count+=1
        # print(count)
        return count
