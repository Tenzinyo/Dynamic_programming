""" 
    reach position x in a matrix-> get number of ways
    combinatory
    example:
        m*n -> 3*5
        f(0,0) = 0
        f(1,1) -> x = 1 
        f(2,2) -> x x = 2 -> f(1,2) , f(2,1)
                  x x 
        f(3,3) -> 
            x x x
            x x x
            x x x
        f(i,j) = f(i-1,j) + f(i,j-1)
        x x x x x
        x x x x x
        x x x x x
        
        curve ball -> 
        there are some raod blocks -> cells not allowed to step
        if matrix(i,j) == blocks[i,j] = 0 
        
        find the most profitable path
            1 3 1 1 2
            2 1 1 1 1
            5 4 4 2 1
            max(f([i-1],[j])+f([i],[j-1])) + f(i,j)
        
    
"""
def unique_path(row,col):
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[0][0] = 1
    for i in range(row):
        for j in range(col): 
            # if dp[i][j] == blocks[i][j]:
            #     dp[i][j] = 0 
            if i==0 and j==0:
                continue
            if i>0 and j>0:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
            elif i>0:
                dp[i][j] = dp[i-1][j]
            elif j>0:
                dp[i][j] = dp[i][j-1]
            
    print(dp[row-1][col-1])
            
unique_path(3,4)

def unique_path_with_profit(grid):
    row = len(grid)
    col = len(grid[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[0][0] = grid[0][0]
    for i in range(row):
        for j in range(col):
            if i==0 and j==0:
                continue
            if i>0 and j>0:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + grid[i][j]
            elif i>0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            elif j>0:
                dp[i][j] = dp[i][j-1] + + grid[i][j]
    print(dp[row-1][col-1])
    
unique_path_with_profit([[0,2,2,50],[5,1,1,100],[4,4,2,0]])
    
def unique_path_with_obstacles(grid):
    row = len(grid)
    col = len(grid[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]
    dp[0][0] = 1
    for i in range(row):
        for j in range(col):
            if i==0 and j==0:
                continue
            if dp[i][j] == 1:
                dp[i][j] = 0
                continue
            if i>0 and j>0:
                dp[i][j] = dp[i-1][j]+ dp[i][j-1] 
            elif i>0:
                dp[i][j] = dp[i-1][j]
            elif j>0:
                dp[i][j] = dp[i][j-1]
    print(dp[row-1][col-1])