class Solution:
    def reorderLogFiles(self, logs):
        letters, digits = [], []

        # 1. 문자인지 숫자인지 구분
        for log in logs:
            # 두 번째 단어가 숫자로만 구성된 경우 -> 숫자 로그
            if log.split()[1].isdigit():
                digits.append(log)
            else:  # 그 외는 문자 로그
                letters.append(log)

        # 2. 문자 로그 정렬
        # (본문을 우선 비교, 동일하다면 식별자 비교)
        letters.sort(key=self.sort_key)  # 'lambda' 대신 별도의 함수 사용

        # 3. 문자 로그 + 숫자 로그 합쳐서 반환
        return letters + digits

    # 2. 문자 로그 정렬을 위한 기준 함수
    def sort_key(self, log):
        # 본문을 기준으로, 본문이 같으면 식별자 기준으로 정렬
        return (log.split()[1:], log.split()[0])
