class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        lett = {}
        for c in magazine:
            lett[c] = lett.get(c,0)+1

        for c in ransomNote:
            if lett.get(c,0) == 0:
                return False 
            lett[c] -=1
        return True