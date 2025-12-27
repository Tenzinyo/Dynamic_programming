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

"""
    objective
    base case
    recursive function
    order of comp
    location ->  cache
    
"""
# climbing stairs problem with O(1) space 
def climb_stairs_optimized(n):
    """
    _summary_
    [1,1,2,3..]
     a,b,c
       a,b,c
  
    """
    a = 1
    b = 1
    c= 0
    for i in range(2,n+1):
        c = a+b
        a = b
        b = c
    print(c)

climb_stairs_optimized(6)

def climb_k_steps(n,k):
    """
    obj -> get the number of steps to reach k steps
    base case ->   
        f(0) = k = 0 , f(0) = 1
        f(1) = k = 1, 0->1 = 1
        f(2) = k = 2, 0 -> 2 = 2
        f(k) = k = k, 0 -> k = f(k-1) + f(k-2)
        
    recursive func -> f(n-1) + f(n-2) + .... + f(n-k)
    
    """
    # space -> O(k) -> mod function to space of k
    dp = [0] * (k)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1): # O(n)
        for j in range(1,k): # O(k)
            if i-j<0:
                continue
            dp[i%k] += dp[(i-j)%k]
    print(dp[n%k])
climb_k_steps(5,2)

def climb_k_steps_avoid_red(n,k,red):
    """
    objective -> climb stairs from n-k and avoid red
    base_case -> n=7, k=3, red = [1,3,4]
    recursive func = f(n-1) + f(n-2) + .. f(n-k)
    
    0 1 2 3 4 5 6 7
      r   r r
    1 0 1 0 0 1 1 2 -> 2 ways to get to the top
   
    """
    dp = [0] * k
    dp[0] = 1
    red_Set = set(red)
    for i in range(0,n+1):
        for j in range(1,k):
            if i-j<0:
                continue
            if i in red_Set:
                dp[i%k] = 0
                continue
            else:
                dp[i%k] += dp[(i-j)%k]
    print(dp[n%k])
climb_k_steps_avoid_red(7,3,[1,3,4])

# optimization problem -> minimize or maximise
""" 
    n = 3, k=2, price = [3,2,4]
    0 1 2 3
      3 2 4 price
    
    objective -> f(i) is cheapest to get to i within k steps
    base case -> 
        f(0) = 0
        f(1) = 3
        f(2) = 5 or 2 = 2
        f(3) = 7 or 6 = 6
    recursive function -> 
        f(n) = p(n) + min(p(n-1),p(n-2))
    order of op -> bottom up
"""
def paid_staircase(n,price):
    dp = [0] * (n+1) #space = O(n)
    dp[0] = 0
    dp[1] = price[1]
    for i in range(2,n+1): #O(n)
        dp[i] = min(dp[i-1],dp[i-2]) + price[i]
    print(dp[n])
paid_staircase(3,[0,3,2,4])