def climb_stairs(n: int) -> int:
    if n <= 1:
        return 1
        
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]


def rob(nums: list[int]) -> int:
    if not nums: return 0
    if len(nums) == 1: return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        rob_current = nums[i] + dp[i-2]
        skip_current = dp[i-1]
        
        dp[i] = max(rob_current, skip_current)
        
    return dp[-1]


# Advanced Memory Optimization:
# Notice that to calculate `dp[i]` we ONLY need `dp[i-1]` and `dp[i-2]`.
# We don't actually need to store the entire array of history!
def rob_optimized(nums: list[int]) -> int:
    prev_max = 0    # i-2
    curr_max = 0    # i-1
    
    for x in nums:
        temp = max(x + prev_max, curr_max)
        prev_max = curr_max
        curr_max = temp
        
    return curr_max


if __name__ == "__main__":
    print("Ways to climb 5 steps:", climb_stairs(5))
    
    houses = [2,7,9,3,1]
    print("Max money to rob:", rob(houses)) 
    print("Max money to rob (O(1) space):", rob_optimized(houses))
