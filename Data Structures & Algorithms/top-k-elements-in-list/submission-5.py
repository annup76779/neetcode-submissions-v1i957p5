class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for num in nums:
            frequency_map[num] = 1 + frequency_map.get(num, 0)
        return [item[0] for item in sorted(frequency_map.items(), key=lambda x: x[1])[len(frequency_map.values()) - k:]]
                
