class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul_num = 1
        has_zero = False

        for i in nums:
            if i == 0 and not has_zero:
                has_zero = True
            else:
                mul_num *= i

        print(mul_num)

        output = []
        for i in nums:
            if has_zero and i == 0:
                res = mul_num
            elif not has_zero:
                res = self.divide(mul_num, i)
            else:
                res = 0

            output.append(res)

        return output

    def divide(self, divident: int, divisor: int):
        if divident == 0: return 0

        is_positive = (divident >= 0) == (divisor >= 0)

        a, b = abs(divident), abs(divisor)
        quotient = 0

        for i in range(a.bit_length(), -1, -1):
            if (b << i) <= a:
                a -= (b << i)
                quotient += (1 << i)

        return quotient if is_positive else -quotient

