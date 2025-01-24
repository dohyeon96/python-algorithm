
class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = []

        # 문자열 소문자로 바꾸기
        S = s.lower()

        for i in S:
            if i.isalnum(): # 문자열이 알파벳이나 숫자인지 판별
                answer += i


        reversed_ansewr = answer[:] # 깊은 복사하기
        reversed_ansewr.reverse()

        # 팰린드롬 판별
        if answer == reversed_ansewr:
            return True
        else:
            return False


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))