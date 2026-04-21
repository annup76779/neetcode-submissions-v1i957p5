class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for sorted_item, item in ((tuple(sorted(i)), i) for i in strs):
            if sorted_item in hash_map.keys():
                hash_map[sorted_item].append(item)
            else:
                hash_map[sorted_item] = [item, ]
        return list(hash_map.values())