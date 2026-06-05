"""
╔══════════════════════════════════════════════════════════════════════════════╗
║          Floyd's Tortoise & Hare — Complete Teaching Implementation          ║
║                  Data Structures & Algorithms · Week 03                      ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT IS THIS FILE?
──────────────────
This file is your complete reference implementation for Floyd's Cycle-Finding
Algorithm. Every function is annotated line-by-line so you can read the code
like a textbook. Run the file directly (python floyd_tortoise_hare.py) to see
each algorithm in action with printed traces.

CONTENTS
────────
  Part 0 · Building blocks  (Node, LinkedList)
  Part 1 · has_cycle()       — detect whether a cycle exists         O(N) / O(1)
  Part 2 · find_cycle_entry() — locate where the cycle begins        O(N) / O(1)
  Part 3 · find_middle()     — find the middle node of any list      O(N) / O(1)
  Part 4 · Demo & tests      — runnable examples with printed output

ALGORITHM SUMMARY
──────────────────
Floyd's Tortoise & Hare uses TWO pointers that travel through the list at
different speeds:

    • Slow pointer (tortoise) — moves 1 node per iteration
    • Fast pointer (hare)     — moves 2 nodes per iteration

Key insight:
    ┌─ No cycle  → the fast pointer reaches None (end of list).
    └─ Cycle     → the fast pointer laps the slow pointer and they COLLIDE.

Why must they collide?
    Once both pointers are inside the loop, the hare gains exactly 1 node on
    the tortoise per iteration (2 steps – 1 step = net gain 1). Starting from
    any gap d ≤ L (loop length), after exactly d iterations the gap reaches 0.

Complexity:
    Time  — O(N)  · each node is visited at most a constant number of times.
    Space — O(1)  · only two pointer variables; no extra data structures.
"""


# ─────────────────────────────────────────────────────────────────────────────
# PART 0 · BUILDING BLOCKS
# ─────────────────────────────────────────────────────────────────────────────

class Node:
    """
    A single element of a singly linked list.

    Fields
    ──────
    data : any value stored at this position in the list.
    next : reference to the next Node, or None if this is the last node.
    """

    def __init__(self, data):
        self.data = data   # payload — what the node stores
        self.next = None   # pointer — where to go next (None = end of list)

    def __repr__(self):
        # Makes debugging easier: print(node) shows Node(42) instead of
        # a cryptic memory address.
        return f"Node({self.data!r})"


class LinkedList:
    """
    A simple singly linked list with helpers used throughout this file.

    The list only holds a reference to the HEAD (first node).
    Every other node is reached by following .next pointers from the head.
    """

    def __init__(self):
        self.head = None   # empty list — no nodes yet

    # ── append ──────────────────────────────────────────────────────────────
    def append(self, data):
        """
        Add a new node with `data` at the END of the list.

        Walk from head to the last node (where .next is None), then link
        in the new node. Time: O(N).
        """
        new_node = Node(data)

        if self.head is None:
            # List is empty — the new node becomes the head.
            self.head = new_node
            return

        # Walk to the last node.
        current = self.head
        while current.next:          # keep going while there IS a next node
            current = current.next   # move one step forward

        current.next = new_node      # hang the new node off the last node

    # ── make_cycle ──────────────────────────────────────────────────────────
    def make_cycle(self, entry_index):
        """
        FOR TESTING: Force the last node's .next to point back to the node
        at position `entry_index` (0-based), creating a cycle.

        Example: make_cycle(1) on  [1 → 2 → 3 → 4]
                 becomes             1 → 2 → 3 → 4 → (back to 2)
        """
        if self.head is None:
            return

        # Find the last node and the target entry node simultaneously.
        entry_node = None
        current = self.head
        index = 0

        while current.next:
            if index == entry_index:
                entry_node = current   # remember the target
            current = current.next
            index += 1

        # `current` is now the last node.
        if entry_index == index:
            entry_node = current       # entry is the last node itself

        current.next = entry_node      # create the cycle

    # ── print_list ──────────────────────────────────────────────────────────
    def print_list(self, limit=20):
        """
        Print the list up to `limit` nodes (guards against infinite loops
        if the list has a cycle).
        """
        elements = []
        current = self.head
        count = 0

        while current and count < limit:
            elements.append(str(current.data))
            current = current.next
            count += 1

        suffix = " → …(cycle)" if count == limit else " → None"
        print("  " + " → ".join(elements) + suffix)


# ─────────────────────────────────────────────────────────────────────────────
# PART 1 · HAS CYCLE — does a cycle exist?
# ─────────────────────────────────────────────────────────────────────────────

def has_cycle(head):
    """
    Determine whether a linked list contains a cycle.

    Parameters
    ──────────
    head : Node | None
        The first node of the list (or None for an empty list).

    Returns
    ───────
    bool — True if a cycle exists, False otherwise.

    Complexity
    ──────────
    Time  O(N)  — at most N + L iterations (prefix + one loop traversal).
    Space O(1)  — only two pointer variables (slow, fast).

    How It Works — Step by Step
    ───────────────────────────
    1. Guard against trivially short lists that cannot have a cycle.
    2. Place slow at head, fast one step ahead (head.next).
    3. Each iteration:
         · fast checks if it has reached the end (no cycle → return False).
         · slow advances 1 step.
         · fast advances 2 steps.
    4. If slow == fast (same node object), they have collided → cycle exists.
    """

    # ── Step 1: edge-case guard ──────────────────────────────────────────────
    # An empty list or a list with a single node cannot form a cycle.
    # Checking here also prevents NoneType errors in the loop below.
    if head is None or head.next is None:
        return False

    # ── Step 2: initialise the two pointers ─────────────────────────────────
    slow = head        # tortoise — will move 1 step per iteration
    fast = head.next   # hare     — starts 1 ahead; will move 2 steps
    #
    # NOTE: Why does fast start at head.next and not head?
    #   If both started at head, the while condition (slow != fast) would be
    #   False immediately, and we would return True for any list — WRONG.
    #   Starting fast one node ahead avoids that false positive.

    # ── Step 3: advance until collision or end ──────────────────────────────
    while slow != fast:
        #
        # Check whether the hare has reached (or is about to reach) the end.
        # This only happens when there is NO cycle — in a cycle, None is
        # never reached because every node always has a next.
        if fast is None or fast.next is None:
            return False           # hare found the end → no cycle

        slow = slow.next           # tortoise: 1 step forward
        fast = fast.next.next      # hare:     2 steps forward

    # ── Step 4: collision ───────────────────────────────────────────────────
    # The while loop exited because slow == fast.
    # They are pointing to the same node object → cycle confirmed.
    return True


# ─────────────────────────────────────────────────────────────────────────────
# PART 2 · FIND CYCLE ENTRY — where does the cycle begin?
# ─────────────────────────────────────────────────────────────────────────────

def find_cycle_entry(head):
    """
    Return the node at which the cycle begins, or None if there is no cycle.

    Parameters
    ──────────
    head : Node | None

    Returns
    ───────
    Node | None — the entry node of the cycle, or None.

    Complexity
    ──────────
    Time  O(N)  — two linear passes (Phase 1 + Phase 2).
    Space O(1)  — two pointer variables throughout.

    The Two-Phase Algorithm
    ───────────────────────
    PHASE 1 — Detect a collision (same as has_cycle).
              Uses slow (1×) and fast (2×) starting from head.

    PHASE 2 — Find the entry point.
              Reset ONE pointer back to head.
              Advance BOTH pointers at speed 1×.
              They will meet exactly at the cycle's entry node.

    Why Phase 2 Works (mathematical proof sketch)
    ──────────────────────────────────────────────
    Let:
        F = number of nodes before the cycle (prefix length)
        L = length of the cycle
        a = position inside the cycle where Phase 1 collision occurs

    At the collision point:
        slow has taken  F + a  steps total.
        fast has taken  F + a + k·L  steps (lapped k times, k ≥ 1).

    Since fast moves twice as fast:
        2(F + a) = F + a + k·L
        F + a = k·L
        F = k·L − a

    After Phase 2 (reset slow to head, both advance 1 step):
        After F steps, slow reaches the cycle entry (it walked the prefix).
        After F steps, fast is at position (a + F) mod L = (a + k·L − a) mod L = 0.
        Position 0 inside the cycle IS the cycle entry.
        ∴ they meet at the entry. ∎
    """

    # ── Edge case ────────────────────────────────────────────────────────────
    if head is None or head.next is None:
        return None

    # ── Phase 1: find the collision point ────────────────────────────────────
    slow = head
    fast = head

    while True:
        # Check for end-of-list (no cycle)
        if fast is None or fast.next is None:
            return None

        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps

        if slow == fast:
            break   # collision found — exit Phase 1

    # At this point slow == fast == the collision node (inside the cycle).

    # ── Phase 2: find the entry node ─────────────────────────────────────────
    slow = head         # reset slow all the way back to the head
    #                     fast stays at the collision node

    while slow != fast:
        slow = slow.next   # both move 1 step
        fast = fast.next   # both move 1 step

    # They have now converged on the cycle entry node.
    return slow   # (slow == fast at this point — either works)


# ─────────────────────────────────────────────────────────────────────────────
# PART 3 · BONUS — FIND THE MIDDLE NODE (same two-pointer trick)
# ─────────────────────────────────────────────────────────────────────────────

def find_middle(head):
    """
    Return the middle node of the linked list.

    For an even-length list, returns the SECOND middle node.
    (e.g. [1,2,3,4] → node(3))

    Parameters
    ──────────
    head : Node | None

    Returns
    ───────
    Node | None — the middle node, or None for an empty list.

    Complexity
    ──────────
    Time  O(N)  — single pass.
    Space O(1)  — two pointer variables.

    How It Works
    ────────────
    Same two-pointer approach, but we stop as soon as fast reaches the end.

        • slow moves 1 step per iteration.
        • fast moves 2 steps per iteration.

    When fast cannot move any further (it is at the last node or None),
    slow is exactly at the midpoint — because it has covered half the
    distance that fast covered.
    """

    if head is None:
        return None

    slow = head
    fast = head

    # Stop when fast has reached the last node (fast.next is None)
    # or gone past it (fast is None).
    while fast and fast.next:
        slow = slow.next        # 1 step
        fast = fast.next.next   # 2 steps

    # slow is now at the middle.
    return slow


# ─────────────────────────────────────────────────────────────────────────────
# PART 4 · DEMO & TESTS
# ─────────────────────────────────────────────────────────────────────────────

def separator(title):
    width = 60
    print("\n" + "─" * width)
    print(f"  {title}")
    print("─" * width)


def demo_has_cycle():
    separator("DEMO 1 · has_cycle()")

    # ── Test A: no cycle ─────────────────────────────────────────────────────
    ll = LinkedList()
    for v in [1, 2, 3, 4, 5]:
        ll.append(v)

    print("\n[A] Linear list (no cycle):")
    ll.print_list()
    result = has_cycle(ll.head)
    print(f"    has_cycle() → {result}   ✓ expected False")

    # ── Test B: cycle at index 1 (node 2) ────────────────────────────────────
    ll2 = LinkedList()
    for v in [1, 2, 3, 4, 5]:
        ll2.append(v)
    ll2.make_cycle(1)   # last node points back to node at index 1 (value=2)

    print("\n[B] Cycle: tail → node(2):")
    ll2.print_list()
    result2 = has_cycle(ll2.head)
    print(f"    has_cycle() → {result2}   ✓ expected True")

    # ── Test C: entire list is a loop (cycle at index 0) ─────────────────────
    ll3 = LinkedList()
    for v in [10, 20, 30]:
        ll3.append(v)
    ll3.make_cycle(0)   # tail → head

    print("\n[C] Full loop: tail → head:")
    ll3.print_list()
    result3 = has_cycle(ll3.head)
    print(f"    has_cycle() → {result3}   ✓ expected True")

    # ── Test D: single node, no cycle ─────────────────────────────────────────
    single = Node(99)
    print("\n[D] Single node (no cycle):")
    print(f"    has_cycle() → {has_cycle(single)}   ✓ expected False")

    # ── Test E: empty list ────────────────────────────────────────────────────
    print("\n[E] Empty list (None):")
    print(f"    has_cycle() → {has_cycle(None)}   ✓ expected False")


def demo_find_cycle_entry():
    separator("DEMO 2 · find_cycle_entry()")

    # ── Test A: cycle at index 2 ──────────────────────────────────────────────
    ll = LinkedList()
    for v in [1, 2, 3, 4, 5, 6, 7]:
        ll.append(v)
    ll.make_cycle(2)   # tail (7) → node at index 2 (value = 3)

    print("\n[A] List 1→2→3→4→5→6→7→(back to 3):")
    ll.print_list()
    entry = find_cycle_entry(ll.head)
    print(f"    find_cycle_entry() → {entry}   ✓ expected Node(3)")

    # ── Test B: cycle at index 0 (full loop) ─────────────────────────────────
    ll2 = LinkedList()
    for v in [5, 6, 7, 8]:
        ll2.append(v)
    ll2.make_cycle(0)   # tail → head (value = 5)

    print("\n[B] Full loop: 5→6→7→8→(back to 5):")
    ll2.print_list()
    entry2 = find_cycle_entry(ll2.head)
    print(f"    find_cycle_entry() → {entry2}   ✓ expected Node(5)")

    # ── Test C: no cycle ──────────────────────────────────────────────────────
    ll3 = LinkedList()
    for v in [1, 2, 3]:
        ll3.append(v)

    print("\n[C] No cycle: 1→2→3→None:")
    ll3.print_list()
    entry3 = find_cycle_entry(ll3.head)
    print(f"    find_cycle_entry() → {entry3}   ✓ expected None")


def demo_find_middle():
    separator("DEMO 3 · find_middle()")

    # ── Odd length ────────────────────────────────────────────────────────────
    ll = LinkedList()
    for v in [1, 2, 3, 4, 5]:
        ll.append(v)
    print("\n[A] Odd length  [1, 2, 3, 4, 5]:")
    ll.print_list()
    mid = find_middle(ll.head)
    print(f"    find_middle() → {mid}   ✓ expected Node(3)")

    # ── Even length ───────────────────────────────────────────────────────────
    ll2 = LinkedList()
    for v in [1, 2, 3, 4]:
        ll2.append(v)
    print("\n[B] Even length  [1, 2, 3, 4]:")
    ll2.print_list()
    mid2 = find_middle(ll2.head)
    print(f"    find_middle() → {mid2}   ✓ expected Node(3) (second middle)")

    # ── Single node ───────────────────────────────────────────────────────────
    single = Node(42)
    print("\n[C] Single node [42]:")
    print(f"    find_middle() → {find_middle(single)}   ✓ expected Node(42)")


def demo_verbose_trace():
    """
    Prints a step-by-step trace of the slow and fast pointers
    so students can see exactly how they move.
    """
    separator("DEMO 4 · Verbose pointer trace on a cyclic list")

    # Build: 1 → 2 → 3 → 4 → 5 → (back to 3)
    ll = LinkedList()
    for v in [1, 2, 3, 4, 5]:
        ll.append(v)
    ll.make_cycle(2)  # tail (5) → node at index 2 (value = 3)

    print("\nList: 1 → 2 → 3 → 4 → 5 → (back to 3)")
    print(f"\n{'Step':<8} {'Slow':<12} {'Fast':<12} {'Status'}")
    print("-" * 48)

    slow = ll.head
    fast = ll.head.next
    step = 0

    print(f"{'Start':<8} {slow.data!s:<12} {fast.data!s:<12} {'initialised'}")

    while slow != fast:
        if fast is None or fast.next is None:
            print("  → Fast reached end. No cycle.")
            return

        slow = slow.next
        fast = fast.next.next
        step += 1
        status = "COLLISION! 🎯" if slow == fast else ""
        print(f"{step:<8} {slow.data!s:<12} {fast.data!s:<12} {status}")

    print(f"\n  ✓ Cycle detected! Slow and Fast met at Node({slow.data}).")


# ─────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  Floyd's Tortoise & Hare — Live Demo")
    print("  Data Structures & Algorithms · Week 03")
    print("=" * 60)

    demo_has_cycle()
    demo_find_cycle_entry()
    demo_find_middle()
    demo_verbose_trace()

    print("\n" + "=" * 60)
    print("  All demos complete.")
    print("=" * 60)


# ─────────────────────────────────────────────────────────────────────────────
# STUDENT EXERCISES
# ─────────────────────────────────────────────────────────────────────────────
#
# Once you understand the code above, try these on your own:
#
# 1. [Easy]   Modify has_cycle() to also RETURN the meeting node (not just True).
#             This sets you up for find_cycle_entry() naturally.
#
# 2. [Medium] Implement find_cycle_length(head) → int:
#             After detecting a collision, keep slow fixed and count how many
#             steps it takes for fast to lap back to the same node.
#
# 3. [Medium] Implement nth_from_end(head, n) → Node:
#             Move fast n steps ahead, then advance both at 1×.
#             When fast reaches None, slow is at the target. O(N) / O(1).
#
# 4. [Hard]   Solve LeetCode 287 "Find the Duplicate Number":
#             You are given an array of N+1 integers in the range [1, N].
#             Treat array[i] as a "pointer" to the next index.
#             There is exactly one duplicate — find it with Floyd's algorithm.
#             Constraint: O(N) time, O(1) space, no modifying the array.
#
# ─────────────────────────────────────────────────────────────────────────────
