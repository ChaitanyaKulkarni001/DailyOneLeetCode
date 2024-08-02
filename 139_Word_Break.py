class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict = {}
        def checker(s,wordDict):
            if s == "":
                return True
            if s in dict:
                return dict[s]
            i=0
            while i <= len(s):
                # print(s[i:len(s)])
                if (s[0:i] in wordDict) and checker(s[i:len(s)],wordDict):
                    dict[s]= True
                    return True    
                i+=1
                dict[s]= False
                
            return False
        
        return checker(s,wordDict)

# Solution 2
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        wordset = set(wordDict)
        for i in range(1,len(s)+1):
            for j in range(i):
                # print(s[j:i])
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        # print(dp)
        return dp[-1]
