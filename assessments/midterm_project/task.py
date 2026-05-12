"""
Task data class for the Task Scheduler Simulation Engine.

This module is PROVIDED to students — do not modify.
Study the __lt__ and __eq__ methods carefully; they define how
tasks compare and therefore how sorting behaves.
"""

from copy import deepcopy


class Task:
    """
    Represents a schedulable unit of work.

    Attributes
    ----------
    task_id : int
        Unique identifier for the task.
    name : str
        Human-readable label.
    priority : int
        Priority level (1 = highest, 10 = lowest).
    deadline : int
        Timestamp by which the task should complete (lower = more urgent).
    duration : int
        Estimated execution time in arbitrary units.
    status : str
        One of "pending", "running", "completed", "cancelled".
    """

    VALID_STATUSES = {"pending", "running", "completed", "cancelled"}

    def __init__(self, task_id: int, name: str, priority: int,
                 deadline: int, duration: int):
        if priority < 1 or priority > 10:
            raise ValueError(f"Priority must be 1–10, got {priority}")
        if duration < 1:
            raise ValueError(f"Duration must be ≥ 1, got {duration}")

        self.task_id = task_id
        self.name = name
        self.priority = priority
        self.deadline = deadline
        self.duration = duration
        self.status = "pending"

    # ---- Comparison operators (enable sorting) ----

    def __lt__(self, other):
        """
        Composite comparison key:
          1. Lower priority NUMBER is higher priority  → sort ascending.
          2. If tied, earlier deadline wins             → sort ascending.

        This is what merge sort will use to decide ordering.
        """
        if self.priority != other.priority:
            return self.priority < other.priority
        return self.deadline < other.deadline

    def __eq__(self, other):
        """Two tasks are equal if they share the same task_id."""
        if not isinstance(other, Task):
            return NotImplemented
        return self.task_id == other.task_id

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    # ---- Display ----

    def __repr__(self):
        return (f"Task(id={self.task_id}, name='{self.name}', "
                f"pri={self.priority}, deadline={self.deadline}, "
                f"dur={self.duration}, status='{self.status}')")

    def __str__(self):
        status_icons = {
            "pending": "⏳",
            "running": "▶️",
            "completed": "✅",
            "cancelled": "❌",
        }
        icon = status_icons.get(self.status, "❓")
        return (f"{icon}  [{self.task_id:03d}] {self.name:<20} "
                f"P={self.priority}  D={self.deadline}  "
                f"Dur={self.duration}  ({self.status})")

    # ---- Deep copy support ----

    def copy(self):
        """Return a deep copy of this task (safe for undo snapshots)."""
        return deepcopy(self)
