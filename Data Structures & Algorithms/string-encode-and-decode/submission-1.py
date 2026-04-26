class Solution:

    def encode(self, strs: List[str]) -> str:
        return ";".join(strs) + ";" if len(strs) else ""

    def decode(self, s: str) -> List[str]:
        k = s.split(";")
        if len(k) > 1:
            k.pop()
            return k
        else:
            return []