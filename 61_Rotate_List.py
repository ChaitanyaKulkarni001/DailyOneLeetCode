# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        # values = np.array(0)
        values = []
        while temp :
            # print(temp.val)
            values.append(temp.val)
            temp = temp.next
        # print(values)
        
        new_values = copy.deepcopy(values)
        # print(new_values)
        length = len(values)
        for i in range(len(values)):
            print(i+k)
            # if i+k >= length:
            new_values[(i+k)%length] = values[i]

        # print(new_values)
        
        temp = head
        # values = np.array(0)
        # values = []
        i=0
        while temp :
            # print(temp.val)
            temp.val = new_values[i]
            i+=1
            temp = temp.next
        return head
        # temp = head
        # values = []
        # print("After values : ",end= " ")
        # while temp :
        #     # print(temp.val)
        #     print (temp.val,end=" ")
        #     temp = temp.next
