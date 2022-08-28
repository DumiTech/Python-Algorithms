"""
Given two strings s and t, return true if t is an anagram of s, and false 
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.
"""

from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sol 1 
        # if (len(s)) != len(t): 
        #     return False
        # list_s, list_t = [], []
        # for i in range(len(s)):
        #     list_s.append(s[i])
        #     list_s.append(t[i])
        # return list_s.sort() == list_t.sort()


        # Sol 2 Using Hash maps (dictionaries in Python)
        # if (len(s)) != len(t): 
        #     return False
        # hash_s, hash_t = {}, {}

        # for i in range(len(s)):
        #     hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
        #     hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        # if (hash_s != hash_t): 
        #     return False
            
        # return True


        # Sol 3 Using one hash map
        if (len(s)) != len(t): 
            return False
        hash_s = {}
        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_s[t[i]] = hash_s.get(t[i], 0) - 1
        #     print(s[i], "=>",hash_s[s[i]])
        #     print()
        # print(hash_s)

        for i in range(len(hash_s)):
            if hash_s.get(s[i], 0) != 0:
                return False

        return True


        # Sol 4 return string as reversed sorted list
        # return sorted(s, reverse=True) == sorted(t, reverse=True)


        # Sol 5 Dict subclass for counting hashtable items
        # elements are stored as dict keys while their counts are stored as values  
        # return Counter(s) == Counter(t)

# s, t= "anagram", "nagaram"
s, t= "rat", "car"
obj = Solution()
print(obj.isAnagram(s,t))