""" 
    coin change: givrn an unlimited supply of coins of given denominations
    find total number of ways to make a change of size n
    
    example -> 
    1 3 5 10
    target = 
        1 1 1 1 1 1
        1 1 1 3
        3 1 1 1
        5 1
        3 3
    objective function = f(i) for i ways to get target
    base case - f(0) = 1
                f(1) = 1 -> 1
                f(2) = 1 -> 1+1
                f(3) = 2 -> 1+1+1, 3
                f(4) = 1|3 3|1 
                    f(3) + f(1) = 2+1 = 3

                f(5) = 5
                    1|4 , 3|2, 5|0
                    f(4) + f(2) + f(0) = 3+1+1 = 5
                f(6) = 5
     
    recursive function - f(n) = f(n-1) + f(n-3) + f(n-5) + f(n-10)
    apporach = bottom up
    location of result = f(n) 
    
"""
def coin_change(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        if i>=1:
            dp[i] += dp[i-1]
        if i>=3:
            dp[i] += dp[i-3]
        if i>=5:
            dp[i] += dp[i-5]
        if i>=10:
            dp[i] += dp[i-10]
        # dp[i] = dp[n-1] + dp[i-3] + dp[i-5] + dp[i-10]
    print(dp[n])
    
coin_change(4)    

def coin_change_with_denomination(n,coins):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
       for coin in coins:
            if i-coin>=0:
                dp[i] += dp[i-coin] 
    print(dp[n])
    
coin_change_with_denomination(4,[1,3,5,10]) 

  
    