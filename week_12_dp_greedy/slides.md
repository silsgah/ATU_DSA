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

---

# 3. Bitmask DP & TSP
When states require tracking a subset of visited nodes (e.g. Traveling Salesperson Problem):
- We represent the subset using a bitmask (an integer where the $i$-th bit represents if vertex $i$ is visited).
- **State Representation**: $dp(mask, u)$ is the minimum cost to visit all vertices in $mask$, ending at vertex $u$.
- **Complexity**:
  - Total states: $N \cdot 2^N$.
  - Transition: from $(mask, u)$ we try all unvisited neighbors $v \notin mask$ ($O(N)$ choices).
  - Time Complexity: $O(N^2 2^N)$.
  - Space Complexity: $O(N 2^N)$.

---

# 4. Matroid Theory & Greedy Optimality
Matroid theory provides mathematical proof for when greedy choices yield optimal results:
- A Matroid is a pair $(S, \mathcal{I})$ where $S$ is a finite set, and $\mathcal{I}$ is a collection of independent subsets of $S$ satisfying:
  1. **Hereditary Property**: If $A \in \mathcal{I}$ and $B \subseteq A$, then $B \in \mathcal{I}$.
  2. **Exchange Property**: If $A, B \in \mathcal{I}$ and $|A| < |B|$, there exists $x \in B \setminus A$ such that $A \cup \{x\} \in \mathcal{I}$.
- **Rado-Edmonds Theorem**: The greedy algorithm finds a maximum-weight independent set in $(S, \mathcal{I})$ if and only if $(S, \mathcal{I})$ is a matroid (e.g. Kruskal's algorithm on graphic matroids).
