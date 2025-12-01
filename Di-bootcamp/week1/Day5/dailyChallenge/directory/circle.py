
import math


class Circle:
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    # ✅ Compute area
    def area(self) -> float:
        return math.pi * self.radius ** 2

    # ✅ Print circle attributes
    def __str__(self) -> str:
        return f"Circle(radius={self.radius}, area={self.area():.2f})"

    __repr__ = __str__

    # ✅ Add two circles (new circle with new radius)
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self.radius + other.radius)

    # ✅ Compare which circle is bigger
    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

    # ✅ Compare equality
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    # ✅ Allow sorting of circles
    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius


if __name__ == "__main__":
    # DEMO

    c1 = Circle(3)
    c2 = Circle(5)
    c3 = Circle(2)

    print("Circle 1:", c1)
    print("Circle 2:", c2)
    print("Circle 3:", c3)

    print("\n--- Area ---")
    print("Area c1:", c1.area())

    print("\n--- Addition ---")
    c4 = c1 + c2
    print("c1 + c2 =", c4)

    print("\n--- Comparisons ---")
    print("c1 > c2:", c1 > c2)
    print("c1 == c2:", c1 == c2)

    print("\n--- Sorting ---")
    circles = [c1, c2, c3, c4]
    circles.sort()
    print("Sorted circles:", circles)
