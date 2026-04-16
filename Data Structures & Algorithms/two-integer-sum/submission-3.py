class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            new_target = target - n
            if new_target in nums_map.keys():
                return [nums_map[new_target], i]
            nums_map[n] = i

        return [-1, -1]
