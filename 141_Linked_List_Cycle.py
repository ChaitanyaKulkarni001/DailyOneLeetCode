# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        flag = True
        retur = False
        address = []
        whileloop = True
        if head is None:
            whileloop = False
            retur = False
        if whileloop:
    
            while head.next is not None and flag:
                if id(head) in address:
                    retur = True
                    flag = False
                address.append(id(head))
                head = head.next
                if head is None:
                    retur = False
                    flag = False
        # print(retur)
        return retur
