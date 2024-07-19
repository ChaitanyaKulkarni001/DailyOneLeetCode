class Solution:
    def calculate(self, s: str) -> int:

        i = 0
        stack = []
        number = 0
        sum = 0
        sign = 1 # 0 1 
        # print("I is",i)
        while i < len(s):
            # sum = 0
            # sign = 1
            if s[i] == "+":
                # stack.append("+")
                # if s[i+1]
                sign = 1
                i+=1
            # print(i)
            # print("while")
            # print(s[i+1])
            # print(s)
            elif s[i] == "-":
                sign = -1
                i+=1
            
            elif s[i] == "(":
                # print("YEs")
                stack.append(sum)
                stack.append(sign)
                sum = 0
                sign =1 
                i+=1
                # continue
            # if s[i] in ["1", "2", "3","4","5","6","7","8","9","0"]:
            elif s[i].isdigit():
                number = 0
                # i+=1
                # while s[i] in ["1", "2", "3","4","5","6","7","8","9","0"]:
                while i<len(s) and s[i].isdigit():
                    # print("Inside while loop")
                    number = number *10+int(s[i])
                    i+=1
                # number = int(number)
                sum += number * sign
                # i-=1
                # sum += number
                # continue
                
                # print(stack)
                # print(i)
                
            # else:
            elif s[i] == ")":
                sum *= stack.pop()
                sum += stack.pop()
                i+=1
            else:
                i+=1       
        return sum
