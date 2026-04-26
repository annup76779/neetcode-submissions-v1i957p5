class Solution:

    def encode(self, strs: List[str]) -> str:
        nums = []

        for i in strs:
            l = str(len(i))
            nums.append(l)
            nums.append(";")
            nums.append(i)

        return "".join(nums)

    def decode(self, s: str) -> List[str]:
        i = 0
        solution = []

        while i < len(s):
            j = 0
            while ";" != s[i+j]:
                j += 1
            l = int(s[i:i+j])
            i += j+1
            ss = s[i:i+l]
            i+=l
            solution.append(ss)

        return solution

