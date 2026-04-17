---
marp: true
theme: default
paginate: true
---

# Week 12: Advanced DP & Greedy
**Data Structures & Algorithms Curriculum**

---

# Focus of the Week
1. 2D Dynamic Programming Grids
2. Multiple State Variables
3. Greedy Algorithms
4. DP vs Greedy Tradeoffs

---

# 1. 2D Dynamic Programming
- Standard 1D DP tracks one shifting constraint. What if you have two?
- Example: "You have 5 weight capacity remaining AND 3 items left to look at."
- Solution: You build an $M \times N$ matrix grid instead of a 1D Array. Exploring down adjusts one constraint, exploring right adjusts the other.

---

# 2. Greedy Algorithms
- DP explores *every single valid branching path* using recursion/matrices to find the guaranteed maximum.
- **Greedy** simply makes the smartest localized choice right here, right now, hoping it leads to a global maximum.
- Usually extremely fast ($O(N \log N)$), but can be structurally unsafe if early "good" choices prevent later "great" choices.

---

# You Have Reached the End!
**Congratulations on completing the Data Structures & Algorithms Curriculum!**
- Time for practical mock interviews!
- Keep profiling your code!
