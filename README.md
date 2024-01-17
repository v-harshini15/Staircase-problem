You are climbing a stair case and it takes A steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Input Format:
The first and the only argument contains an integer A, the number of steps.
Output Format:
Return an integer, representing the number of ways to reach the top.
Constrains:
1 <= A <= 36
If the number of steps is 1 or less, there is only one way to climb (no steps or one step).

Initialize an array dp to store the number of ways to reach each step.

There is 1 way to reach the first step (dp[1] = 1).

There are 2 ways to reach the second step (dp[2] = 2), either by taking 1 step + 1 step or 2 steps.

Use dynamic programming to calculate the number of ways for each step starting from the third step.

The final result is stored in dp[A], representing the number of ways to climb A steps.

In the example, the algorithm determines that there are 2 ways to climb 2 steps and 3 ways to climb 3 steps.
