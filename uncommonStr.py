class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        #code here
        res = set(s1) - set(s2)
        res1 = set(s2) - set(s1)
        out = res.union(res1)
        my_str =  [str(i) for i in out]
        out_str = ''.join(my_str)
        return sorted(out_str)