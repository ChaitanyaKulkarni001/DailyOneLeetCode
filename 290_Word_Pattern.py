# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution:
  def wordPattern(pattern, s):
      words = s.split()
      
      if len(pattern) != len(words):
          return False
      
      patm = {}
      wordm = {}
      
      for a, word in zip(pattern, words):
          if a not in patm:
              patm[a] = word
          if word not in wordm:
              wordm[word] = a
          
          if patm[a] != word or wordm[word] != a:
              return False
      
