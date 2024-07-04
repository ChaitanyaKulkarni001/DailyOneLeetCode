class Solution:
    def intToRoman(self, num: int) -> str:
        myDuck = {
        
        1 :'I',
        5 :'V',
        10 :'X',
        50 :'L',
        100 :'C',
        500 :'D',
        1000 :'M'
    }
        divisors = [1000,500,100,50,10,5,1]
        myDuck2={
            4:'IV',
            9:'IX',
            40:'XL',
            90:'XC',
            400:'CD',
            900:'CM'
        }
        # num = 58
        nonGeneral = [4,9,40,90,400,900]

        
    # print(type(s(tr))

        lists = []
        i=1
        while num>0:
            lists.append(num%10*i)
            num = num//10
            i*=10
        lists = lists[::-1]
        finish = ""
        for i in lists:
            k=0
            while i:
                j = divisors[k]
                # print(" j:",j)
                if i in nonGeneral:
                    finish+=f"{myDuck2[i]}"
                    break
                    
                if i/j>=1:
                    finish+=f"{myDuck[j]}"
                    # print("finish : ",finish)
                    i = i-j
                    # print(" i :",i)
                    # print(i)
                else:
                    k+=1
                    # print(" i :",i)
                    # print(" k :",k)
        return finish
