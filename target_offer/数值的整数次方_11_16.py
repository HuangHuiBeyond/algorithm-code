# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0.0 and exponent < 0:
            return 0.0
        abs_exponent = abs(exponent)
        result = self.powerWithUnsignedExponent(base, abs_exponent)
        if exponent < 0:
            result = 1 / result
        return result

    # def powerWithUnsignedExponent(self, base, abs_exponent):
    #     result = 1
    #     for _ in range(1, abs_exponent + 1):
    #         result *= base
    #     return result

    def powerWithUnsignedExponent(self, base, abs_exponent):
        if abs_exponent == 0:
            return 1
        if abs_exponent == 1:
            return base
        result = self.powerWithUnsignedExponent(base, abs_exponent >> 1)
        result *= result
        if abs_exponent & 0x1 == 1:
            result *= base
        return result
sol = Solution()
print(sol.Power(3, -2))