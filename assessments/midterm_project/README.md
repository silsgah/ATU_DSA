# 📋 Midterm Project: Task Scheduler Simulation Engine

## Data Structures & Algorithms — Weeks 4–10 Assessment

**Weight**: 30% of Final Grade  
**Due**: [Insert Date]  
**Submission**: Push to your GitHub repository under `midterm_project/`

---

## 🎯 Overview

You will build a **Task Scheduler Simulation Engine** — a system that models how an operating system manages, prioritises, and executes tasks. This project exercises **stacks**, **queues**, **sorting algorithms**, and **merge sort** in a single, cohesive application.

Your scheduler will:
1. Accept tasks with priorities and deadlines
2. Schedule them using a priority queue (sorted via merge sort)
3. Execute tasks using a stack-based call model
4. Track execution history using a queue-based event log
5. Support an **undo/redo** mechanism via dual stacks

This is not a toy exercise — real operating systems and job schedulers (cron, Kubernetes, Airflow) use exactly these patterns.

---

## 📐 Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    TaskScheduler                         │
│                                                          │
│  ┌──────────────┐   ┌──────────────┐   ┌─────────────┐  │
│  │  Task Queue   │   │ Execution    │   │ Undo/Redo   │  │
│  │  (Priority    │──▶│ Stack        │──▶│ Stacks      │  │
│  │   sorted via  │   │ (Call Stack  │   │ (Action     │  │
│  │   merge sort) │   │  model)      │   │  history)   │  │
│  └──────────────┘   └──────────────┘   └─────────────┘  │
│         │                                     │          │
│         ▼                                     ▼          │
│  ┌──────────────┐                    ┌─────────────┐     │
│  │ Event Log     │                    │ Statistics   │     │
│  │ (FIFO Queue)  │                    │ Reporter     │     │
│  └──────────────┘                    └─────────────┘     │
└──────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
midterm_project/
├── README.md                  ← You are here
├── task.py                    ← Task data class
├── scheduler.py               ← Core scheduler (IMPLEMENT THIS)
├── merge_sort.py              ← Merge sort implementation (IMPLEMENT THIS)
├── undo_redo.py               ← Undo/Redo manager (IMPLEMENT THIS)
├── event_log.py               ← FIFO event logger (IMPLEMENT THIS)
├── main.py                    ← Demo driver + interactive CLI
├── test_scheduler.py          ← Automated test suite
└── REPORT.md                  ← Your analysis report (WRITE THIS)
```

---

## 🔧 Part 1: The Task (5 marks)

The `Task` class is provided for you in `task.py`. Study it carefully — it defines the data your scheduler will manage.

Each task has:
- `task_id` — unique identifier
- `name` — human-readable label
- `priority` — integer (1 = highest priority, 10 = lowest)
- `deadline` — integer timestamp (lower = more urgent)
- `duration` — estimated execution time in units
- `status` — one of `"pending"`, `"running"`, `"completed"`, `"cancelled"`

**Your job**: In your report, explain why `__lt__` and `__eq__` are defined on the Task class, and how they enable sorting.

---

## 🔧 Part 2: Merge Sort for Priority Scheduling (20 marks)

**File**: `merge_sort.py`

Implement merge sort to sort tasks by a **composite key**:
1. Primary sort: by `priority` (ascending — lower number = higher priority)
2. Secondary sort (tie-breaker): by `deadline` (ascending — earlier deadline first)

### Requirements
- Implement `merge_sort(tasks)` → returns a new sorted list
- Implement `merge(left, right)` → merges two sorted halves
- **Do NOT use Python's built-in `sorted()` or `.sort()`** — that defeats the purpose
- Add complexity comments: Time and Space for each function

### Bonus (5 marks)
- Implement a **counting version** `merge_sort_counted(tasks)` that also returns the total number of comparisons made during sorting. This helps you empirically verify the O(N log N) bound.

---

## 🔧 Part 3: The Execution Stack (20 marks)

**File**: `scheduler.py`

The scheduler maintains an **execution stack** — a LIFO structure that models how an OS runs tasks (like a function call stack).

### Required Methods

```python
class TaskScheduler:
    def __init__(self):
        """Initialise the scheduler with:
        - A task queue (list of pending tasks)
        - An execution stack (list used as LIFO stack)
        - An event log (EventLog instance)
        - An undo/redo manager (UndoRedoManager instance)
        """

    def add_task(self, task):
        """Add a task to the queue. Re-sort the queue using YOUR merge sort.
        Log the event. Push to undo stack."""

    def execute_next(self):
        """Pop the highest-priority task from the queue.
        Push it onto the execution stack. Set status to 'running'.
        Log the event. Push to undo stack."""

    def complete_current(self):
        """Pop the top task from the execution stack.
        Set status to 'completed'. Log the event. Push to undo stack."""

    def preempt(self, new_task):
        """Interrupt: push the currently-running task back onto the queue,
        and start executing new_task instead. This models OS preemption.
        Log the event. Push to undo stack."""

    def get_queue_snapshot(self):
        """Return a copy of the current task queue (sorted order)."""

    def get_stack_snapshot(self):
        """Return a copy of the current execution stack."""
```

### Key Constraints
- The **queue** must always remain sorted by priority (using your merge sort)
- The **execution stack** follows strict LIFO — `execute_next()` pushes, `complete_current()` pops
- Every state-changing operation must be logged and undoable

---

## 🔧 Part 4: Event Log — FIFO Queue (15 marks)

**File**: `event_log.py`

Implement a circular queue to store event history. The log has a fixed capacity — when full, the oldest event is overwritten (like a ring buffer).

### Requirements

```python
class EventLog:
    def __init__(self, capacity=100):
        """Fixed-size circular queue for event records."""

    def log(self, event_type, task, details=""):
        """Enqueue a new event. If at capacity, overwrite the oldest."""

    def get_recent(self, n=10):
        """Return the N most recent events (dequeue order)."""

    def get_all(self):
        """Return all events in chronological order."""

    def __len__(self):
        """Number of events currently stored."""
```

Each event should be a dictionary:
```python
{
    "timestamp": <auto-incrementing int>,
    "event_type": "ADDED" | "STARTED" | "COMPLETED" | "PREEMPTED" | "CANCELLED" | "UNDO" | "REDO",
    "task_id": <int>,
    "task_name": <str>,
    "details": <str>
}
```

---

## 🔧 Part 5: Undo/Redo Manager — Dual Stacks (15 marks)

**File**: `undo_redo.py`

Implement an undo/redo system using **two stacks** — this is exactly how text editors and IDEs implement Ctrl+Z / Ctrl+Y.

### Requirements

```python
class UndoRedoManager:
    def __init__(self):
        """Two stacks: undo_stack and redo_stack.
        Each entry stores a snapshot of the scheduler state."""

    def save_state(self, state):
        """Push current state onto undo stack. Clear the redo stack
        (new action invalidates the redo history)."""

    def undo(self):
        """Pop from undo stack, push current state to redo stack.
        Return the restored state, or None if nothing to undo."""

    def redo(self):
        """Pop from redo stack, push current state to undo stack.
        Return the restored state, or None if nothing to redo."""

    def can_undo(self):
        """Return True if undo is possible."""

    def can_redo(self):
        """Return True if redo is possible."""
```

### State Snapshot
A state is a dictionary capturing:
```python
{
    "queue": [list of tasks],
    "stack": [list of tasks],
    "action": "description of what happened"
}
```

**Important**: You must deep-copy the lists when saving state — otherwise undo will restore references to mutated objects.

---

## 🔧 Part 6: Interactive Demo & Statistics (10 marks)

**File**: `main.py`

Build a command-line interface that lets the user interact with the scheduler:

```
=== Task Scheduler Simulation Engine ===
1. Add Task
2. Execute Next Task
3. Complete Current Task
4. Preempt with New Task
5. View Queue
6. View Execution Stack
7. View Event Log
8. Undo
9. Redo
10. Run Sorting Benchmark
11. Exit
> _
```

The **Sorting Benchmark** (option 10) should:
1. Generate random task lists of sizes: 100, 500, 1000, 5000, 10000
2. Sort each using YOUR merge sort
3. Print a table of: input size, time taken, comparisons made
4. Verify that growth follows O(N log N)

---

## 📝 Part 7: Analysis Report (15 marks)

**File**: `REPORT.md`

Write a structured report covering:

### Section A: Complexity Analysis (5 marks)
- Time and space complexity for every method you implemented
- Justify each with a brief proof or argument

### Section B: Sorting Empirical Analysis (5 marks)
- Table of benchmark results (size, time, comparisons)
- Plot or describe the growth curve
- Compare empirical results to theoretical O(N log N) — do they match?

### Section C: Design Decisions (5 marks)
- Why is the undo/redo system implemented with two stacks instead of one?
- Why is the event log a circular queue instead of an unbounded list?
- What happens if you use `sorted()` instead of merge sort? What do you lose pedagogically?
- Describe one real-world system that uses a pattern from this project

---

## ✅ Grading Rubric

| Component | Marks | Criteria |
|---|---|---|
| **Merge Sort** | 20 | Correct divide-conquer-combine, handles edge cases, composite key |
| **Execution Stack** | 20 | LIFO behaviour, preemption, correct state transitions |
| **Event Log (Queue)** | 15 | Circular buffer, overwrite semantics, chronological ordering |
| **Undo/Redo (Stacks)** | 15 | Dual-stack pattern, deep copy, undo clears redo |
| **Interactive Demo** | 10 | CLI works, benchmark runs, output is readable |
| **Report** | 15 | Complexity analysis, empirical data, design justification |
| **Code Quality** | 5 | Naming, comments, structure, no use of forbidden built-ins |
| **Total** | **100** | |

---

## ⚠️ Rules & Constraints

1. **No built-in sorting**: Do not use `sorted()`, `.sort()`, `heapq`, or `collections.deque` for the core data structures. Implement from scratch.
2. **No external libraries**: Only the Python standard library (`copy`, `time`, `random` for benchmarks).
3. **Meaningful names**: Use `prev`, `current`, `next_node` — not `x`, `y`, `z`.
4. **Complexity comments**: Every function must have a comment stating its Time and Space complexity.
5. **Edge cases**: Handle empty queues, empty stacks, undo with nothing to undo, single-task scenarios.
6. **Academic integrity**: This is individual work. Cite any referenced material.

---

## 🚀 Getting Started

```bash
# Run the automated tests
python3 test_scheduler.py

# Run the interactive demo
python3 main.py
```

Start with `merge_sort.py` → `event_log.py` → `undo_redo.py` → `scheduler.py` → `main.py`.

Build bottom-up. Test each module independently before integrating.

---

## 📚 Concepts Exercised

| Week | Topic | Where It Appears |
|---|---|---|
| Week 4 | Stacks (LIFO) | Execution stack, undo/redo stacks |
| Week 4 | Queues (FIFO) | Event log circular queue |
| Week 4 | Circular Queue | Event log ring buffer |
| Week 10 | Merge Sort | Priority scheduling, benchmark |
| Week 10 | Divide & Conquer | Merge sort decomposition |
| General | Sorting | Composite key sorting, stability |

Good luck — and remember: **the right data structure makes the algorithm obvious.**
