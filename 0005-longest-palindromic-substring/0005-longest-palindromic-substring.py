class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬을 확인하고 확장하는 함수 정의
        def expand(left: int, right: int) -> str:
            # 문자열 경계 내에서 좌우 포인터가 가리키는 문자가 같을 동안 확장
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  # 왼쪽 포인터를 왼쪽으로 이동
                right += 1  # 오른쪽 포인터를 오른쪽으로 이동
            # 유효한 팰린드롬 문자열 반환
            return s[left + 1:right]

        # 문자열이 너무 짧거나 이미 팰린드롬인 경우 빠르게 결과 반환
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''  # 가장 긴 팰린드롬 부분 문자열을 저장할 변수 초기화

        # 문자열의 각 위치를 기준으로 팰린드롬 확장을 시도
        for i in range(len(s) - 1):
            # 짝수 길이 팰린드롬 확장
            # 현재 위치(i)와 바로 다음 위치(i + 1)를 기준으로 팰린드롬 확장
            # 예: "abba"에서 i=1이면 expand(1, 2)는 "abba"를 찾음
            expand_result_even = expand(i, i + 1)

            # 홀수 길이 팰린드롬 확장
            # 현재 위치(i)와 그다음 위치(i + 2)를 기준으로 팰린드롬 확장
            # 예: "racecar"에서 i=3이면 expand(3, 4)는 "racecar"를 찾음
            expand_result_odd = expand(i, i + 2)

            # 현재 위치에서 가장 긴 팰린드롬을 찾고, 결과를 업데이트
            # 이전까지의 결과(result)와 현재 위치에서의 짝수, 홀수 팰린드롬 중 가장 긴 것을 선택
            # max 함수에서 key=len을 사용해 길이가 가장 긴 문자열을 반환
            result = max(result, expand_result_even, expand_result_odd, key=len)


        # 가장 긴 팰린드롬 부분 문자열 반환
        return result