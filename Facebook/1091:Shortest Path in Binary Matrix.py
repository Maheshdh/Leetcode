class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if(grid[0][0] or grid[rows-1][cols-1]):
            return -1

        queue = collections.deque()
        queue.append((0,0,1))
        dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        grid[0][0] = 1
        while queue:
            x,y,dist = queue.popleft()
            if(x == rows-1 and y == cols-1):
                return dist
            for x_inc, y_inc in dirs:
                x_new, y_new = x+x_inc, y+y_inc
                if(0<=x_new<rows and 0<=y_new<cols) and (grid[x_new][y_new]==0):
                    queue.append((x_new,y_new,dist+1))
                    grid[x_new][y_new] = 1
        return -1
            
