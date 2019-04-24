class Solution(object):
    # ===============1========================== 24ms?28ms?
#     def transformer(self, word):
#         trans  = ""
#         letter = "abcdefghijklmnopqrstuvwxyz"
#         moses  = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#         for w in word:
#             i = letter.index(w)
#             trans += moses[i]
#         return trans
    
#     def uniqueMorseRepresentations(self, words):
#         """
#         :type words: List[str]
#         :rtype: int
#         """
#         repre = []
#         for word in words:
#             trans = self.transformer(word)
#             if trans not in repre:
#                 repre.append(trans)
#         return len(repre)

    # ================2=========================== 24ms
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letter = "abcdefghijklmnopqrstuvwxyz"
        moses  = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        dic = {}
        for l,m in zip(list(letter), moses):
            dic[l]=m
        
        repre = []
        for word in words:
            w=""
            for i in word:
                w += dic[i]
            repre.append(w)
        return len(set(repre))
