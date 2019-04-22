class Solution:
    # Given a valid parentheses string S like "()(())", take off the coat parentheses and output remained parentheses
    # input: S, for ex, "()(())"
    # output: out, for ex, "()"
    
    def removeOuterParentheses(self, S: str) -> str:
        # let's define sum=0, everytime encounter a "(" we plus 1, a ")" we minus 1;
        # since a valid parentheses string S always begin with "(", let's ignore the first "(" but do the sum at the sametime; 
        # from the second index: 
        #   if ")" then sum gets to 0, then this is a coat parenthese that we must take off, so we won't copy it to the output string out
        #   if "(" then sum gets to 2, then we copy the "(" to the output string out
        #     exception: if the sum gets to 1, that means we've encounted a coat parenthese and this "(" is just a new begin of a pair, so we shouldn't copy it
        
        s = 0
        out = ""
        for i in range(len(S)):
            if i == 0:
                s += 1
            
            else:
                if S[i]=="(":
                    s += 1
                    if s != 1:
                        out += S[i]
                
                else:
                    s += -1
                    if s != 0:
                        out += S[i]            
        return out
        
# ========================================================================        
# There's another solution from a leetcode user @jkbielan which I found also interesting:
class Solution:
	def removeOuterParentheses(self, S: str) -> str:
		parts = []
		left_n = 0
		right_n = 0

		# [j+1:i] will be slice getting parts without beginning and end
		j = 0  

		for i in range(len(S)):
			if S[i] == "(":
				left_n += 1  # add 1 when left parenthesis
			else:
				right_n += 1  # add 1 when right

			if left_n == right_n:
				parts.append(S[j + 1:i])  # add part when left_n = right_n
				j = i + 1  # because next first item will be cut, i + 1 gives j += 2 total
