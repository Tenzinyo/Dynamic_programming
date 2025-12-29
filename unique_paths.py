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

def get_path(grid):
    """ 

        x x x
        x x x    
    """
    row = len(grid)
    col = len(grid[0])
    dp = [[0 for _ in range(col)] for _ in range(col)]
    path = []
    r,c = row-1,col-1
    for i in range(row):
        for j in range(col):
            if i==0 and j==0:
                continue
            if i>0 and j>0:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1]) + grid[i][j]
            elif i>0:
                dp[i][j] = dp[i-1][j]
            elif j>0:
                dp[i][j] = dp[i][j-1]
    
    while r>=0 and c>=0:
        path.append((r,c))
        if r==0 and c==0:
            break
        if r>0 and c>0:
            if dp[r-1][c] > dp[r][c-1]:
                r-=1
            else:
                c-=1
        elif r>0:
            r-=1
        elif c>0:
            c-=1   
    path.reverse()
    print(path)
get_path([[0,2,2,1],[3,1,1,1],[4,4,2,0]])


def paint(n):
    """ 
        objective function -> paint the house and make sure that the adjacent houses dont have same color
        base case -> 
            f(i) 4->  0 0 0 1 -> blue = 0 green = 1
                    f(i-1) = needs to be blue
                    f(i-2) = needs to be green
                    f(i-3) = needs to be blue lets have j as the color 
                    the next j is the opositite of color before = 1-j 
        recursive function = f(i,j) = f(i-1,1-j) + f(i-2,1-j)
                    
    """
    dp = [[0 for _ in range(2)] for _ in range(n+1)]
    dp[1][0] = 1
    dp[1][1] = 1 
    dp[2][0] = 2
    dp[2][1] = 2 
    for i in range(3,n+1):
         for j in range(2):
             dp[i][j] = dp[i-1][1-j] + dp[i-2][1-j]
    print(dp[n][0] + dp[n][1])
paint(5)

def subsets(nums):
    """ 
        f(0) = []
        f(1) = f(0) + f(1)
        f(2) = f(0) + f(1) + f(2)
        f(3) = f(0) + f(1) + f(2) + f(3)
    """
    n = len(nums)
    dp = [[]]*(n+1)
    dp[0] = [[]]
    for i in range(1,n+1):
        prev = dp[i-1]
        result = []
        for p in prev:
            result.append(p+[nums[i-1]])
            dp[i] = prev+result
    return dp[n]

            
    
  