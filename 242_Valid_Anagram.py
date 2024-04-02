# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s= list (s)
        t= list (t)
        try:
            for i in s:
                t.remove(i)
            if t==[]:
                return True
            return False
        except Exception as e:
            return False
