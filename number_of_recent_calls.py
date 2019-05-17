########################
# this is really a bad problem, a waste of time; 
# it's actually a simple question, but it's not well explained; 
# all my time spent on understanding what he says, not happy

class RecentCounter:

    def __init__(self):
        self.query = []

    def ping(self, t: int) -> int:
        self.query.append(t)
        # self.query = [a for a in self.query if t-3000 <= a <= t ]
        # return len(self.query)
        # Time limit exceeded
        
        while self.query[0] < t-3000:
            self.query.pop(0)
        return len(self.query)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
