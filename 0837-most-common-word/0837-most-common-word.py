from typing import List
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word = ''
        word_list = []
        lowercase_paragraph = paragraph.lower()

        # 단어를 추출하여 리스트로 저장
        for i in range(len(lowercase_paragraph)):
            if "a" <= lowercase_paragraph[i] <= "z":
                word += lowercase_paragraph[i]
            else:
                if word:  # 단어가 완성된 경우만 리스트에 추가
                    word_list.append(word)
                    word = ''  # 단어 초기화
        if word:  # 마지막 단어 처리
            word_list.append(word)

        # 금지된 단어를 제외하고 빈도 계산
        # 해시 테이블 기반 자료구조 set -> list보다 검색 속도 빠름
        banned_set = set(banned)
        word_count = Counter([w for w in word_list if w not in banned_set])

        # value(값)을 기준으로 가장 빈도가 높은 단어 반환
        return max(word_count, key=word_count.get)