def climbStairs(A):
    if A <= 1:
        return 1
    
    # Initialize an array to store the number of ways to reach each step
    dp = [0] * (A + 1)
    
    # There is 1 way to reach the first step
    dp[1] = 1
    
    # There are 2 ways to reach the second step (1 step + 1 step or 2 steps)
    dp[2] = 2
    
    # Calculate the number of ways for each step starting from the third step
    for i in range(3, A + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[A]

# Example 1
A1 = 2
result1 = climbStairs(A1)
print(result1)  # Output: 2

# Example 2
A2 = 3
result2 = climbStairs(A2)
print(result2)  # Output: 3
