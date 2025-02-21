class Solution:
    def reorderLogFiles(self, logs):
        letters = []
        digits = []

        # 1. 로그를 문자 로그와 숫자 로그로 분리
        for log in logs:
            if log.split()[1].isdigit():  # 숫자 로그일 경우
                digits.append(log)
            else:  # 문자 로그일 경우
                letters.append(log)

        # 2. 문자 로그 정렬하기
        # 문자 로그는 본문을 기준으로 정렬하고, 본문이 동일하면 식별자 순으로 정렬
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                log1 = letters[i]
                log2 = letters[j]

                # 본문 비교 (log.split()[1:])
                # 본문이 다르면, 본문 기준으로 정렬
                if log1.split()[1:] > log2.split()[1:]:
                    letters[i], letters[j] = letters[j], letters[i]
                elif log1.split()[1:] == log2.split()[1:]:
                    # 본문이 같으면 식별자(log.split()[0]) 기준으로 정렬
                    if log1.split()[0] > log2.split()[0]:
                        letters[i], letters[j] = letters[j], letters[i]

        # 3. 정렬된 문자 로그 + 숫자 로그를 이어서 반환
        return letters + digits
