"""
Dog Class Module.
"""

from cat import Cat


class Dog:
    """Dog Class"""

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def bark(self) -> None:
        """Barks."""
        print(f"{self.name} barks.")

    def meet(self, other):
        """Handles meeting others."""
        if isinstance(other, Dog):
            print(f"{self.name} wags tail at {other.name}")

        if isinstance(other, Cat):
            print(f"{self.name} barks at {other.name}")
