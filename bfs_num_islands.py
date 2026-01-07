class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        visited -> set
        queue 

        go through the row and column:
                        we check for neighbour if the current coordinate:
                            we need directions to check for left,right,up and down
                                if currernt coordinate is land:
                                        we want its neighbour to be water
                                        vice versa
        """
        row = len(grid)
        col = len(grid[0])
        num_islands = 0
        visited = set()

        if not grid:
            return 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    num_islands += 1
                    queue = deque([(r,c)])
                    visited.add((r,c))
                    while queue:
                        curr_r,curr_c = queue.popleft()
                        directions = [[-1,0],[0,1],[1,0],[0,-1]]
                        for dr,dc in directions: 
                            nr = curr_r + dr
                            nc = curr_c + dc
                            if 0<=nr<row and 0<=nc<col and grid[nr][nc] == "1" and (nr,nc) not in visited:
                                queue.append((nr,nc))
                                visited.add((nr,nc))
        return num_islands 

        



        