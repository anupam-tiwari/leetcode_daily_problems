class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        first_x, first_y = -1, -1
        for i in range(n): 
            for j in range(n):
                if grid[i][j] == 1: 
                    first_x, first_y = i, j
                    break
        
        #dfs to find other lands 
        def dfs(x, y): 
            bfs_q.append((x,y))
            grid[x][y] = 2
            for i, j in [(x+1,y), (x-1,y), (x,y-1), (x,y+1)]: 
                if 0 <= i < n and 0 <= j < n and grid[i][j] == 1: 
                    dfs(i,j)
        
        bfs_q = []
        dfs(first_x, first_y)

        #bfs
        distance = 0
        while bfs_q: 
            new_q = []
            for i, j in bfs_q: 
                for x,y in [(i+1,j), (i-1,j), (i,j-1), (i,j+1)]: 
                    if 0 <= x < n and 0<= y < n: 
                        if grid[x][y] == 1: 
                            return distance 
                        if grid[x][y] == 0: 
                            new_q.append((x,y))
                            grid[x][y] = -1
            bfs_q = new_q
            distance+=1 
            
        return -1