# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1st. node.val들을 저장해서 앞, 뒤를 비교하기 위해서 list q를 선언
        q: List = []

        # 2nd. 팰린드롬 판별 전에 head가 비어있는지 확인
        if not head:
            return True
        node = head # head 말고 node.val가 익숙하므로 node에 복사

        #3rd. node.val들을 list q에 저장
        while node is not None:
            q.append(node.val)
            node = node.next
        
        #4th. list 앞, 뒤 요소 비교해서 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True
