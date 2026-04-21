from typing import List,Dict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map: Dict[int, tuple[int, int]] = {}
        for num in nums:
            frequency_map[num] = (num, frequency_map.get(num, (num, 0))[1] + 1)
        return list(
            map(
                lambda x: x[0],
                sorted(frequency_map.values(), key=lambda x: x[1])[len(frequency_map.values()) - k:],
            )
        )
