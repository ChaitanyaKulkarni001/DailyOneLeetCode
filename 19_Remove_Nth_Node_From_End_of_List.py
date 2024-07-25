# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        if head == None : return None
        temp = head
        count = 1
        while (temp.next !=None):
            count+=1
            temp = temp.next
        # print(f"Length is {count}")
        
        before_remove_node = count - n
        if before_remove_node == 0:
            if head.next :
                return head.next
            return None
        temp = head
        i=1
        if count == n:
            return None
        while (i!=before_remove_node):
            temp = temp.next
            i+=1
        if (temp.next is None or temp.next.next is None):
            temp.next = None
        else:
            
            temp.next = temp.next.next
        # temp = head
        # while (temp!=None):
        #     print (temp.val,end=" ")
        #     temp = temp.next
        # print(" ")
        return head
