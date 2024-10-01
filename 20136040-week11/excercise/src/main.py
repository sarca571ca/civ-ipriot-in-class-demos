"""
Main entrypoint.
"""

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
        if isinstance(other, Dog):
            print(f"{self.name} hisses at {other.name}")

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

def main():
    """Main function."""
    cat = Cat("Jinx", 5, "white")

    print(f"Name: {cat.name}\tAge: {cat.age}\tCoat color: {cat.coat_color}")
    cat.purr()

    print("\n")

    dog = Dog("Uri", 2)
    print(f"Name: {dog.name}\tAge: {dog.age}")
    dog.bark()

    print("\n")

    cat.meet(dog)
    cat.meet(cat)

    dog.meet(cat)
    dog.meet(dog)

if __name__ == "__main__":
    main()
