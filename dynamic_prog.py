"""
    problem -> sum of first N numbers
    
    obj function - > output
        F(i) is sum of i elements
    
    recurrence relation - > F(n) = F(n-1) + n
"""

def sum_of_n(n):
    dp = [0]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        dp[i] = dp[i-1]+i
    print(dp[n])
sum_of_n(6)

def fibb(n):
    """
    f(5) = f(4) + f(3)
    
        recurssion -> f(n-1) + f(n-2)
    """
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
        print(dp)
    print(dp[n])
fibb(4)

def climb_stairs(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2] 
    print(dp[n])

climb_stairs(4)