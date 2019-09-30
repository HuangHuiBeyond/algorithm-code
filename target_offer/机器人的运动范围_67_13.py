# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 and rows < 1 and cols < 1:
            return 0
        visited = [0] * (rows * cols)

        count = self.movingCountCore(threshold, rows, cols, 0, 0, visited)
        return count
    
    def movingCountCore(self, threshold, rows, cols, row, col, visited):
        count = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row * cols + col] = 1
            count = 1 + self.movingCountCore(threshold, rows, cols, row - 1, col, visited) \
                    + self.movingCountCore(threshold, rows, cols, row + 1, col, visited) \
                    + self.movingCountCore(threshold, rows, cols, row, col - 1, visited) \
                    + self.movingCountCore(threshold, rows, cols, row, col + 1, visited)
        return count

    def check(self, threshold, rows, cols, row, col, visited):
        if row >= 0 and row < rows and col >= 0 and col < cols and self.getDigitSum(row) + self.getDigitSum(col) <= threshold\
            and not visited[row * cols + col]:
            return True
        return False
    
    def getDigitSum(self, num):
        sum_ = 0
        while num > 0:
            sum_ += num % 10
            num //= 10
        return sum_
    
sol = Solution()
res = sol.movingCount(1, 3, 4)
print(res)