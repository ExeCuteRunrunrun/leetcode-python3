class Solution:
    def judgeCircle(self, moves: str) -> bool:
        returned = True
        num_moves = len(moves)
        if num_moves % 2 != 0:
            returned = False
        else:
            dic = {"U":"D", "D":"U", "L":"R", "R":"L"}
            for a in dic:
                if moves.count(a) != moves.count(dic[a]):
                    returned = False
        return returned
        
##############official solution###################
class Solution(object):
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        return x == y == 0
