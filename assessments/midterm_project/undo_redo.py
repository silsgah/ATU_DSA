"""
Undo / Redo Manager — Dual Stacks
===================================
STUDENT IMPLEMENTATION FILE

Implement an undo/redo system using TWO stacks.
This is exactly how text editors implement Ctrl+Z / Ctrl+Y.

Pattern:
  - Every action pushes a state snapshot onto the undo stack.
  - Undo pops from undo → pushes to redo.
  - Redo pops from redo → pushes to undo.
  - A NEW action clears the redo stack (branching invalidates the redo history).

Rules:
  - Implement both stacks using plain Python lists (append/pop).
  - Deep-copy all state when saving — otherwise undo restores mutated references.
  - Add Time / Space complexity comments above each method.
"""

from copy import deepcopy


class UndoRedoManager:
    """
    Manages scheduler state history using two stacks.

    State snapshots are dictionaries:
        {
            "queue":  [list of Task copies],
            "stack":  [list of Task copies],
            "action": "description of what happened"
        }
    """

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def __init__(self):
        """Initialise empty undo and redo stacks."""
        # TODO: Create two empty lists: undo_stack and redo_stack
        pass

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def save_state(self, state: dict):
        """
        Save a state snapshot onto the undo stack.
        Clear the redo stack (new action invalidates redo history).

        Parameters
        ----------
        state : dict
            Must contain keys "queue", "stack", and "action".
            The lists inside MUST be deep-copied before storing.
        """
        # TODO: Implement
        #   1. Deep copy the state dictionary.
        #   2. Push (append) onto undo_stack.
        #   3. Clear the redo_stack (a new action branches the timeline).
        pass

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def undo(self) -> dict | None:
        """
        Undo the last action.

        Returns
        -------
        dict or None
            The restored state snapshot, or None if nothing to undo.

        Side-effects
        -------------
        - Pops from undo_stack.
        - Pushes the popped state onto redo_stack (so it can be re-done).
        """
        # TODO: Implement
        pass

    # -----------------------------------------------------------------
    # Time:  O(?)    Space: O(?)
    # -----------------------------------------------------------------
    def redo(self) -> dict | None:
        """
        Redo the last undone action.

        Returns
        -------
        dict or None
            The re-applied state snapshot, or None if nothing to redo.

        Side-effects
        -------------
        - Pops from redo_stack.
        - Pushes the popped state onto undo_stack.
        """
        # TODO: Implement
        pass

    # -----------------------------------------------------------------
    # Time:  O(1)    Space: O(1)
    # -----------------------------------------------------------------
    def can_undo(self) -> bool:
        """Return True if undo is possible."""
        # TODO: Implement
        pass

    # -----------------------------------------------------------------
    # Time:  O(1)    Space: O(1)
    # -----------------------------------------------------------------
    def can_redo(self) -> bool:
        """Return True if redo is possible."""
        # TODO: Implement
        pass

    def __repr__(self):
        u = len(getattr(self, 'undo_stack', []))
        r = len(getattr(self, 'redo_stack', []))
        return f"UndoRedoManager(undo={u}, redo={r})"


# -----------------------------------------------------------------
# Quick sanity check
# -----------------------------------------------------------------
if __name__ == "__main__":
    mgr = UndoRedoManager()

    # Simulate saving states
    mgr.save_state({"queue": [1, 2, 3], "stack": [], "action": "Added task 1, 2, 3"})
    mgr.save_state({"queue": [2, 3],    "stack": [1], "action": "Executed task 1"})
    mgr.save_state({"queue": [3],       "stack": [1, 2], "action": "Executed task 2"})

    print(f"Manager: {mgr}")
    print(f"Can undo: {mgr.can_undo()}")
    print(f"Can redo: {mgr.can_redo()}")

    # Undo
    state = mgr.undo()
    if state:
        print(f"\nUndo → {state['action']}")
        print(f"  Queue: {state['queue']}")
        print(f"  Stack: {state['stack']}")
    else:
        print("\n(undo not yet implemented)")

    print(f"\nAfter undo — Can redo: {mgr.can_redo()}")

    # Redo
    state = mgr.redo()
    if state:
        print(f"Redo → {state['action']}")
    else:
        print("(redo not yet implemented)")
