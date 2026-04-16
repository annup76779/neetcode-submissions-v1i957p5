class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            new_target = target - nums[i]
            if new_target in nums_map.keys():
                return [nums_map[new_target], i]
            nums_map[nums[i]] = i

        return [-1, -1]
