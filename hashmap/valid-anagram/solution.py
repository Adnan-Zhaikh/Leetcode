class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        ch1 = {}
        ch2 = {}

        for c in s:
            ch1[c] = ch1.get(c,0)+1
        for c in t:
            ch2[c] = ch2.get(c,0) +1

        return ch1 == ch2