class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        f0, f1 = 1, 1   # f(0)=1, f(1)=1
        
        # Compute f(i) iteratively
        for i in range(2, n+1):
            f2 = f1 + f0   # f(i) = f(i-1) + f(i-2)
            f0, f1 = f1, f2  # shift: f(i-1)=f1, f(i-2)=f0
        
        return f1   # final result = f(n)

        