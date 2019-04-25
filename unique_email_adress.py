class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        actual = []
        for email in emails:
            local       = email.split("@")[0]
            domain      = email.split("@")[1]
            # keep string before "+"
            to_be_trans = local.split("+")[0]
            # remove "." in local
            local = to_be_trans.replace(".","")
            email = local+"@"+domain
            actual.append(email)
        # print(actual)
            
        return len(set(actual))
