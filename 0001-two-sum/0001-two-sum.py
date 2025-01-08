class Solution: # 이렇게 주석을 추가하면 더 이해하기 좋을것 같아요
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if target == nums[i] + nums[j]:
                        return [i, j]

        
