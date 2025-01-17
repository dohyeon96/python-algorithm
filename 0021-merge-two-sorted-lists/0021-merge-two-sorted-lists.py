# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """ 
    list1의 다음 노드는 list1의 다음 노드와 list2를 병합한 값으로 설정한다. 
    즉, 이렇게하면 list1은 list2보다 작은 값을 가지게 되고, 
    list1의 다음 노드는 list1의 다음 노드와 list2를 병합한 값
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list2:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
        
        
