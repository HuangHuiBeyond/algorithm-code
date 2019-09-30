class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or rows < 1 or cols < 1 or not path:
            return False
        
        visited = [0] * (rows * cols)

        path_index = 0
        for row in range(rows):
            for col in range(cols):
                if self.has_path_core(matrix, rows, cols, row, col, path, path_index, visited):
                    return True
        return False

    def has_path_core(self, matrix, rows, cols, row, col, path, path_index, visited):
        if len(path) == path_index: ## 递归定义终止条件
            return True
        
        has_path = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] \
            == path[path_index] and not visited[row * cols + col]:
            path_index += 1
            visited[row * cols + col] = True

            has_path =  self.has_path_core(matrix, rows, cols, row - 1, col, path, path_index, visited) or \
                        self.has_path_core(matrix, rows, cols, row + 1, col, path, path_index, visited) or \
                        self.has_path_core(matrix, rows, cols, row, col - 1, path, path_index, visited) or \
                        self.has_path_core(matrix, rows, cols, row, col + 1, path, path_index, visited)
            if not has_path: ## 尝试不成功，回溯，要把状态变量换回来
                path_index -= 1
                visited[row * cols + col] = False
        return has_path ## 返回值

s = Solution()
ifTrue = s.hasPath("abtgcfcsjdeh", 3, 4, "bfce")
ifTrue = s.hasPath("abtgcfcsjdeh", 3, 4, "abfb")
ifTrue = s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS",5,8,"SGGFIECVAASABCEEJIGOEM")

print(ifTrue)