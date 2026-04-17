def longest_common_subsequence(text1: str, text2: str) -> int:
    # Add + 1 to handle the empty string base case implicitly (padding the top and left with zeros)
    rows = len(text1)
    cols = len(text2)
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if text1[r-1] == text2[c-1]:
                # Characters match, take diagonal value and add 1
                dp[r][c] = 1 + dp[r-1][c-1]
            else:
                # Characters don't match, take max of left or top cell
                dp[r][c] = max(dp[r-1][c], dp[r][c-1])
                
    return dp[rows][cols]


def find_content_children(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    
    child_i = 0
    cookie_j = 0
    
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            # This cookie satisfies this child
            child_i += 1
            
        # regardless of whether the cookie satisfied the child or not, 
        # we still move to the next cookie. If it was too small, we try the next biggest one.
        cookie_j += 1
        
    return child_i


if __name__ == "__main__":
    t1 = "abcde"
    t2 = "ace"
    print("LCS of abcde and ace:", longest_common_subsequence(t1, t2)) 
    
    children_greed = [1, 2, 3] 
    cookie_sizes = [1, 1]      
    print("Content children:", find_content_children(children_greed, cookie_sizes)) 
