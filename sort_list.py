# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left=head
        right=self.mid(head)
        tmp=right.next
        right.next=None
        right=tmp
        
        list1=self.sortList(left)
        list2=self.sortList(right)
        return self.merge(list1, list2)
        
        
    def mid(self, head):
        s,f=head,head.next
        while f and f.next:
            s,f=s.next, f.next.next
        return s
    
    def merge(self, list1, list2):
        t=head=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                t.next=list1
                list1=list1.next
            else:
                t.next=list2
                list2=list2.next
            t=t.next
        if list1:
            t.next=list1
        else:
            t.next=list2
        return head.next
        
