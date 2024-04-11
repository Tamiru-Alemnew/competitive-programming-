# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0

        while startValue != target:

            if startValue > target:
                operations += startValue - target - 1
                startValue = target

            elif target % 2 == 0:
                target //= 2
            else:
                target += 1
                
            operations += 1

        return operations
