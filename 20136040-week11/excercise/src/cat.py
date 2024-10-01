"""
Cat class module.
"""

# from dog import Dog


class Cat:
    """Cat Class"""

    def __init__(self, name, age, coat_color) -> None:
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def meow(self) -> None:
        """Meows."""
        print(f'{self.name} says "Meow"')

    def purr(self) -> None:
        """Purrs."""
        print(f"{self.name} purrs.")

    def meet(self, other):
        """Handles meeting others."""
        if isinstance(other, Cat):
            print(f"{self.name} hisses at {other.name}")
        # if isinstance(other, Dog):
        #     print(f"{self.name} hisses at {other.name}")
