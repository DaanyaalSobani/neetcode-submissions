class Solution:
# first pass solution (I know it's not the most efficient)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for letter in s:
            if letter not in s_dict:
                s_dict[letter] = 0
            s_dict[letter] +=1
        for letter in t:
            if letter not in t_dict:
                t_dict[letter] = 0
            t_dict[letter] +=1
        for key, value in s_dict.items():
            if value != t_dict.get(key):
                return False
        return True
        