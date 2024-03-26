# Problem :- Given two strings s and t, determine if they are isomorphic, Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        sdict={}
        tdict={}
        sdictInd={}
        tdictInd={}
        # s="paper"
        # t="title"
        # str="abcd"
        # print(str.index('b')+1)
        strings=""
        stringt=""
        for i in s:
            if i in sdict:
                sdict[i]+=1
                sdictInd[i]=sdictInd[i]+s.index(i)
                strings=strings+str(s.index(i))
            else:
                sdict[i]=1
                sdictInd[i]=s.index(i)


        for i in t:
            if i in tdict:
                tdict[i]+=1
                tdictInd[i]=tdictInd[i]+t.index(i)
                stringt=stringt+str(t.index(i))
            else:
                tdict[i]=1
                tdictInd[i]=t.index(i)

        if str(sdict.values())==str(tdict.values()) and str(sdictInd.values())==str(tdictInd.values())  and strings==stringt:
            # print("Same")
            return True
        else:
            # print("Not same")
            return False
