class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) % 2 == 0:  # 요소가 짝수개면
            for i in range(len(s)):
                if i < len(s) / 2:
                    store = s[i]
                    s[i] = s[len(s) - i - 1]
                    s[len(s) - i - 1] = store
                    store = " "
            print(s)
        else:
            for j in range(len(s)):
                if j < len(s) / 2:
                    store = s[j]
                    s[j] = s[len(s) - j - 1]
                    s[len(s) - j - 1] = store
                    store = " "
            print(s)

        