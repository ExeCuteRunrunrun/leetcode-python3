class Solution(object):
    def toLowerCase(self, S):
        """
        :type str: str
        :rtype: str
        """
        # =================1====================== 20ms
        dic = {"A":"a",
               "B":"b",
               "C":"c",
               "D":"d",
               "E":"e",
               "F":"f",
               "G":"g",
               "H":"h",
               "I":"i",
               "J":"j",
               "K":"k",
               "L":"l",
               "M":"m",
               "N":"n", 
               "O":"o",
               "P":"p",
               "Q":"q",
               "R":"r",
               "S":"s",
               "T":"t",
               "U":"u",
               "V":"v",
               "W":"w",
               "X":"x",
               "Y":"y",
               "Z":"z"}
        out = ""
        for a in S:
            out+=dic.get(a,a)
        return out
        
        # ===================2===================== 28ms
        # return S.lower()
