class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        defaultdict의 목적은 키가 없을 때 발생하는 KeyError를 방지하고, 
        미리 지정한 기본값을 자동으로 할당하여 편리하게 딕셔너리를 관리하는 것입니다.
        """
        """
        dict()와 defaultdict()의 가장 큰 차이점은 키가 없을 때의 동작
        """
        anagrams = collections.defaultdict(list)
        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())