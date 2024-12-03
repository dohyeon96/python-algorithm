class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        forward_list = []

        for i in s:
            if i.isalnum(): # 숫자/알파벳/한글인 경우에 forward_list에 append
                forward_list.append(i) 

        for j in range(0, len(forward_list) - 1):
            if forward_list[j] != forward_list[-j - 1]:
                return False
        return True