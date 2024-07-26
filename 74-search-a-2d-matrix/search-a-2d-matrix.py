class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found=False
        row=0
        print(len(matrix[0]))
        for i in range(len(matrix)):
            
            if target <= matrix[i][len(matrix[0])-1]:
                row=i
                break
        for i in range(len(matrix[row])):
            if target==matrix[row][i]:
                found=True
                break
        return found
    