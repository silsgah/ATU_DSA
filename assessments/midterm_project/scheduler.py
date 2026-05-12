"""
Task Scheduler — Core Engine
==============================
STUDENT IMPLEMENTATION FILE

The TaskScheduler ties together every data structure from this course module:
  - Merge sort   → keeps the task queue in priority order
  - Stack (LIFO) → models the execution call stack
  - Queue (FIFO) → event logging via circular buffer
  - Dual stacks  → undo/redo history

Rules:
  - Use YOUR merge_sort from merge_sort.py (not sorted() or .sort()).
  - Every state-changing method must log the event AND save undo state.
  - Add Time / Space complexity comments above each method.
"""

from copy import deepcopy
from task import Task
from merge_sort import merge_sort
from event_log import EventLog
from undo_redo import UndoRedoManager


class TaskScheduler:
    """
    A priority-based task scheduler with execution stack,
    event logging, and undo/redo support.
    """

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def __init__(self):
        """
        Initialise the scheduler.

        Internal state:
            task_queue      : list[Task]   — pending tasks, kept sorted
            execution_stack : list[Task]   — currently running tasks (LIFO)
            event_log       : EventLog     — circular buffer of events
            undo_redo       : UndoRedoManager — dual-stack history
        """
        # TODO: Initialise
        #   - self.task_queue = []
        #   - self.execution_stack = []
        #   - self.event_log = EventLog(capacity=200)
        #   - self.undo_redo = UndoRedoManager()
        pass

    # ---- Private helpers ----

    def _save_undo(self, action: str):
        """Snapshot current state for undo."""
        # TODO: Build a state dict with deep copies of queue and stack,
        #       then call self.undo_redo.save_state(state)
        pass

    def _resort_queue(self):
        """Re-sort the task queue using YOUR merge sort."""
        # TODO: self.task_queue = merge_sort(self.task_queue)
        pass

    # ---- Public API ----

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def add_task(self, task: Task):
        """
        Add a task to the priority queue.

        Steps:
            1. Save undo state.
            2. Append the task to the queue.
            3. Re-sort the queue using merge sort.
            4. Log an "ADDED" event.
        """
        # TODO: Implement
        pass

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def execute_next(self) -> Task | None:
        """
        Pop the highest-priority task from the queue and push it
        onto the execution stack.

        Returns
        -------
        Task or None
            The task that started executing, or None if queue is empty.

        Steps:
            1. If queue is empty, return None.
            2. Save undo state.
            3. Pop index 0 from the queue (highest priority after sort).
            4. Set task status to "running".
            5. Push onto execution stack.
            6. Log a "STARTED" event.
            7. Return the task.
        """
        # TODO: Implement
        pass

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def complete_current(self) -> Task | None:
        """
        Pop the top task from the execution stack and mark it completed.

        Returns
        -------
        Task or None
            The completed task, or None if stack is empty.

        Steps:
            1. If stack is empty, return None.
            2. Save undo state.
            3. Pop from execution stack.
            4. Set task status to "completed".
            5. Log a "COMPLETED" event.
            6. Return the task.
        """
        # TODO: Implement
        pass

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def preempt(self, new_task: Task) -> Task | None:
        """
        Preempt the currently running task with a higher-priority task.

        This models OS preemptive scheduling: the current task is paused
        and returned to the queue, and the new task starts immediately.

        Parameters
        ----------
        new_task : Task
            The task that will take over execution.

        Returns
        -------
        Task or None
            The preempted (paused) task, or None if stack was empty.

        Steps:
            1. Save undo state.
            2. If execution stack is not empty:
               a. Pop the current task.
               b. Set its status back to "pending".
               c. Add it back to the task queue.
            3. Set new_task status to "running".
            4. Push new_task onto execution stack.
            5. Re-sort the queue.
            6. Log a "PREEMPTED" event.
            7. Return the preempted task (or None).
        """
        # TODO: Implement
        pass

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def cancel_task(self, task_id: int) -> Task | None:
        """
        Remove a task from the queue by ID and mark it cancelled.

        Parameters
        ----------
        task_id : int

        Returns
        -------
        Task or None
            The cancelled task, or None if not found in queue.
        """
        # TODO: Implement
        #   1. Search the queue for a task with matching task_id.
        #   2. If found: save undo, remove it, set status "cancelled",
        #      log "CANCELLED", return it.
        #   3. If not found: return None.
        pass

    # ---- Undo / Redo ----

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def undo(self) -> bool:
        """
        Undo the last action, restoring the previous scheduler state.

        Returns True if undo succeeded, False if nothing to undo.
        """
        # TODO: Implement
        #   1. Call self.undo_redo.undo()
        #   2. If a state was returned, restore self.task_queue and
        #      self.execution_stack from the snapshot.
        #   3. Log an "UNDO" event.
        pass

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def redo(self) -> bool:
        """
        Redo the last undone action.

        Returns True if redo succeeded, False if nothing to redo.
        """
        # TODO: Implement
        pass

    # ---- Accessors ----

    def get_queue_snapshot(self) -> list:
        """Return a copy of the current task queue."""
        return deepcopy(self.task_queue) if hasattr(self, 'task_queue') else []

    def get_stack_snapshot(self) -> list:
        """Return a copy of the current execution stack."""
        return deepcopy(self.execution_stack) if hasattr(self, 'execution_stack') else []

    def get_event_log(self) -> list:
        """Return all logged events."""
        if hasattr(self, 'event_log'):
            return self.event_log.get_all() or []
        return []


# -----------------------------------------------------------------
# Quick sanity check
# -----------------------------------------------------------------
if __name__ == "__main__":
    scheduler = TaskScheduler()

    # Create some tasks
    tasks = [
        Task(1, "Write report",   3, 100, 5),
        Task(2, "Fix critical bug", 1, 30,  2),
        Task(3, "Code review",    2, 80,  3),
        Task(4, "Deploy hotfix",  1, 20,  4),
        Task(5, "Team standup",   3, 90,  1),
    ]

    print("=== Adding tasks ===")
    for t in tasks:
        scheduler.add_task(t)

    print("\nQueue (should be sorted by priority, then deadline):")
    for t in scheduler.get_queue_snapshot():
        print(f"  {t}")

    print("\n=== Executing top task ===")
    executed = scheduler.execute_next()
    if executed:
        print(f"  Now running: {executed}")

    print("\nQueue after execution:")
    for t in scheduler.get_queue_snapshot():
        print(f"  {t}")

    print("\nExecution stack:")
    for t in scheduler.get_stack_snapshot():
        print(f"  {t}")

    print("\n=== Completing current task ===")
    completed = scheduler.complete_current()
    if completed:
        print(f"  Completed: {completed}")

    print("\n=== Undo ===")
    if scheduler.undo():
        print("  Undo successful!")
        print("  Stack after undo:")
        for t in scheduler.get_stack_snapshot():
            print(f"    {t}")
    else:
        print("  (undo not yet implemented)")

    print("\n=== Event Log ===")
    for e in scheduler.get_event_log():
        print(f"  [{e.get('timestamp', '?')}] {e.get('event_type', '?'):>10} — "
              f"{e.get('task_name', '?')}")
