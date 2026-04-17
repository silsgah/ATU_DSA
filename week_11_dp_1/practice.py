# Exercise 1: Climbing Stairs (Bottom-Up DP)
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
def climb_stairs(n: int) -> int:
    # TODO: Build an array of size n+1. (Base cases: dp[0] = 1, dp[1] = 1)
    # The number of ways to reach step `i` is the number of ways to reach `i-1` + ways to reach `i-2`.
    pass


# Exercise 2: House Robber
# You are a professional robber planning to rob houses along a street. Each house has a certain 
# amount of money stashed. You cannot rob adjacent houses, because they have connected security systems.
# Given an integer array nums representing the amount of money of each house, return the maximum 
# amount of money you can rob without alerting the police.
def rob(nums: list[int]) -> int:
    # TODO: DP array where dp[i] represents the max money robbed UP TO house i.
    # For every house i, you have a choice:
    # 1. Rob house i (meaning you add nums[i] to the max money from house i-2)
    # 2. Skip house i (meaning you just take the max money from house i-1)
    # dp[i] = max(rob_this, skip_this)
    pass


if __name__ == "__main__":
    print("Ways to climb 5 steps:", climb_stairs(5)) # Expect 8
    
    houses = [2,7,9,3,1]
    print("Max money to rob:", rob(houses)) # Expect 12 (Rob houses 2, 9, 1)
