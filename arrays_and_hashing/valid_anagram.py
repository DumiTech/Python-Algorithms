"""
Given two strings s and t, return true if t is an anagram of s, and false 
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters exactly once.
"""

from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Sol 1 Using Hash maps (dictionaries in Python)
        if (len(s)) != len(t): 
            return False
        hash_s, hash_t = {}, {}

        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        if (hash_s != hash_t): 
            return False
            
        return True


        # Sol 2 Using one hash map
        # if (len(s)) != len(t): 
        #     return False
        # hash_s = {}
        # for i in range(len(s)):
        #     hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
        #     hash_s[t[i]] = hash_s.get(t[i], 0) - 1
        # #     print(s[i], "=>",hash_s[s[i]])
        # #     print()
        # # print(hash_s)
        
        # for i in range(len(hash_s)):
        #     if hash_s.get(s[i], 0) != 0:
        #         return False

        # return True


        # Sol 3 Using one hash map, but slight different approach
        # dic = {}
        # for i in s:
        #     if i not in dic:
        #         dic[i] = 1
        #     else:
        #         dic[i] += 1

        # for j in t:
        #     if j not in dic:
        #         return False
        #     else:
        #         dic[j] -= 1

        # print(dic.values())
        
        # for val in dic.values():
        #     if val != 0:
        #         return False

        # return True 


        # Sol 4 return string as reversed sorted list
        # return sorted(s, reverse=True) == sorted(t, reverse=True)


        # Sol 5 Dict subclass for counting hashtable items
        # elements are stored as dict keys while their counts are stored as values  
        # return Counter(s) == Counter(t)

        # Sol 6 
        # return all(s.count(i)==t.count(i) for i in set(s+t))

# s, t= "anagram", "nagaram"
s, t= "rat", "car"
obj = Solution()
print(obj.isAnagram(s,t))