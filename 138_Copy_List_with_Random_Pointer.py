"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None: return None
        
        
        
        # duplicate_list = Node(head.val)
        
        new_pointer = head
        do = True
        while new_pointer:
            if do == True:
                do =    False
                node = Node(new_pointer.val)
                prev_pointer = node
                main = prev_pointer
                new_pointer = new_pointer.next
            else:    
                node = Node(new_pointer.val)
                prev_pointer.next = node
                prev_pointer = prev_pointer.next
                new_pointer = new_pointer.next
            
        adrresses_of_original = {}
        temp = head
        i=0
        while temp:
            adrresses_of_original.update({id(temp):i})
            i+=1
            temp=temp.next
        # print(adrresses_of_original)
        temp = head
        another_list = main
        while temp:
            if temp.random:
                address = id(temp.random)
                # print(f"the values is {temp.val} and address is {id(temp)} ")
                # print(address)
                index = adrresses_of_original[address]
                temporary = main
                i = 0
                while i!=index:
                    i+=1
                    temporary = temporary.next
                another_list.random = temporary
            temp = temp.next
            another_list = another_list.next
        return main
            
