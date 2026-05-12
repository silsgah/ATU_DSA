"""
Event Log — FIFO Circular Queue
================================
STUDENT IMPLEMENTATION FILE

Implement a fixed-capacity circular queue that stores scheduler events.
When the queue is full, new events overwrite the oldest (ring buffer).

Rules:
  - Do NOT use collections.deque or any built-in queue.
  - Implement the circular buffer using a plain Python list + head/tail pointers.
  - Add Time / Space complexity comments above each method.
"""


class EventLog:
    """
    A fixed-size circular queue for recording scheduler events.

    Each event is a dictionary with keys:
        timestamp, event_type, task_id, task_name, details
    """

    VALID_EVENTS = {
        "ADDED", "STARTED", "COMPLETED",
        "PREEMPTED", "CANCELLED", "UNDO", "REDO"
    }

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def __init__(self, capacity: int = 100):
        """
        Initialise the circular queue.

        Parameters
        ----------
        capacity : int
            Maximum number of events the log can hold.
        """
        # TODO: Initialise:
        #   - A fixed-size list of `capacity` slots (filled with None)
        #   - head and tail pointers (start at -1 to indicate empty)
        #   - A counter for the current number of stored events
        #   - A monotonically increasing timestamp counter
        pass

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def log(self, event_type: str, task, details: str = ""):
        """
        Record a new event.

        Parameters
        ----------
        event_type : str
            One of VALID_EVENTS.
        task : Task
            The task this event concerns.
        details : str
            Optional extra information.
        """
        # TODO: Implement circular enqueue
        #   1. Validate event_type.
        #   2. Build the event dictionary.
        #   3. Advance the tail pointer using modulo arithmetic.
        #   4. If the queue was empty, also set head = 0.
        #   5. If the queue is full (tail catches head), advance head too
        #      (overwriting the oldest event).
        #   6. Store the event at the tail position.
        #   7. Increment the timestamp counter.
        pass

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def get_recent(self, n: int = 10) -> list:
        """
        Return the N most recent events, newest first.

        Parameters
        ----------
        n : int
            Number of recent events to return.

        Returns
        -------
        list[dict]
            Up to n events in reverse-chronological order.
        """
        # TODO: Implement
        #   Walk backwards from tail for n steps (or until you've
        #   covered all stored events). Use modulo to wrap around.
        pass

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def get_all(self) -> list:
        """
        Return ALL stored events in chronological order (oldest first).

        Returns
        -------
        list[dict]
        """
        # TODO: Implement
        #   Walk from head to tail using modulo arithmetic.
        pass

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def __len__(self) -> int:
        """Return the number of events currently stored."""
        # TODO: Implement
        pass

    def __repr__(self):
        return f"EventLog(capacity={getattr(self, 'capacity', '?')}, stored={len(self)})"


# -----------------------------------------------------------------
# Quick sanity check
# -----------------------------------------------------------------
if __name__ == "__main__":
    from task import Task

    log = EventLog(capacity=5)
    t1 = Task(1, "Alpha", 2, 50, 3)
    t2 = Task(2, "Beta",  1, 30, 2)

    log.log("ADDED", t1)
    log.log("ADDED", t2)
    log.log("STARTED", t2)
    log.log("COMPLETED", t2)
    log.log("STARTED", t1)
    # This 6th event should overwrite the oldest
    log.log("COMPLETED", t1, details="All done")

    print(f"Log: {log}")
    print(f"Length: {len(log)}")
    print("\nAll events:")
    all_events = log.get_all()
    if all_events:
        for e in all_events:
            print(f"  [{e['timestamp']}] {e['event_type']:>10} — {e['task_name']}")
    else:
        print("  (not yet implemented)")

    print("\n2 most recent:")
    recent = log.get_recent(2)
    if recent:
        for e in recent:
            print(f"  [{e['timestamp']}] {e['event_type']:>10} — {e['task_name']}")
    else:
        print("  (not yet implemented)")
