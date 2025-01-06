class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        sum = 0

        for i in range(len(sorted_list)):
            if i%2 == 0:
                sum += sorted_list[i]
        return sum
        