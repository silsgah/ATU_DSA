# Exercise 1: Longest Common Subsequence (2D DP)
# Given two strings text1 and text2, return the length of their longest common subsequence.
# Subsequence means characters don't need to be contiguous. (e.g. "ace" is a subsequence of "abcde")
def longest_common_subsequence(text1: str, text2: str) -> int:
    # TODO: Create a 2D array dp of size (len(text1)+1) x (len(text2)+1).
    # Nested loops: if char matches, dp[i][j] = 1 + dp[i-1][j-1]
    # If not match, dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    pass


# Exercise 2: Assign Cookies (Greedy)
# Assume you are a parent and want to give your children cookies. 
# Each child i has a greed factor g[i], and each cookie j has a size s[j].
# If s[j] >= g[i], the child is content. Output the max number of content children.
def find_content_children(g: list[int], s: list[int]) -> int:
    # TODO: Greedy approach. 
    # 1. Sort both the greed array and cookie size array globally.
    # 2. Iterate simultaneously. If the current cookie satisfies the current child, 
    # increment content count and move to next child and next cookie. 
    # 3. If cookie is too small, move to the next larger cookie.
    pass


if __name__ == "__main__":
    t1 = "abcde"
    t2 = "ace"
    print("LCS of abcde and ace:", longest_common_subsequence(t1, t2)) # Expect 3
    
    children_greed = [1, 2, 3] # One kid needs size 1, one needs 2, etc.
    cookie_sizes = [1, 1]      # We only have two tiny cookies
    print("Content children:", find_content_children(children_greed, cookie_sizes)) # Expect 1
