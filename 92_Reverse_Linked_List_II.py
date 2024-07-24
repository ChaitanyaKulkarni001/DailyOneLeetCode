# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        

        # tail = head
        # while (tail.next!=None):
        #     tail = tail.next()
        left_pointer = head
        right_pointer = head
        i=1
        while i!=left:
            left_pointer = left_pointer.next
            i+=1
        
        i=1
        while i!=right:
            right_pointer = right_pointer.next
            i+=1
        temp = left_pointer
        values = []
        while temp!=right_pointer:
            values.append(temp.val)
            temp=temp.next
        values.append(temp.val)
        # print(values)
        values.reverse()
        # print("REvresed values",values)
        temp = left_pointer
        i=0
        while (temp!=right_pointer):
            temp.val = values[i]
            i+=1
            temp=temp.next
        temp.val = values[i]
        temp = head
        # while (temp!=None):
        #     print (temp.val,end=" ")
        #     temp = temp.next
        return head
            
