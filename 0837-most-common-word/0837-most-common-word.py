class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cleaned_paragraph = ""
        for ch in paragraph:
            if ch.isalnum():
                cleaned_paragraph += ch
            else:
                cleaned_paragraph += " "  # 문장부호나 기타 문자는 공백으로 대체

        # 모두 소문자로 변환
        cleaned_paragraph = cleaned_paragraph.lower()

        # 공백 기준으로 단어 분리
        words = cleaned_paragraph.split()

        # 단어 빈도 계산 (금지 단어 제외)
        word_count = {}
        for word in words:
            if word not in banned:
                word_count[word] = word_count.get(word, 0) + 1

        # 가장 많이 등장하는 단어 찾기
        max_word = ""
        max_count = 0
        for word, count in word_count.items():
            if count > max_count:
                max_count = count
                max_word = word

        return max_word