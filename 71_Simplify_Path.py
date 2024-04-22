# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
# In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.



class Solution:
    def simplifyPath(self, path: str) -> str:
        myStack = []
        parts = path.split('/')
        for part in parts :
            if part == '..' :
                if myStack:
                    myStack.pop()
                
            elif part == '.':
                continue
            elif part == '':
                continue
            else:
                myStack.append(part)
        finalAns = '/' + '/'.join(myStack)
        return finalAns
