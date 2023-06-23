class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def is_valid(row,col):
            val = matrix[row][col]
            while row < len(matrix) and col < len(matrix[0]):
                if(matrix[row][col]!=val):
                    return False
                row += 1
                col += 1
            return True
        
        for col in range(len(matrix[0])):
            if(is_valid(0,col) == False):
                return False
        for row in range(1, len(matrix)):
            if(is_valid(row,0) == False):
                return False
        
        return True
