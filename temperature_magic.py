"""Tools for working with Temperatures."""


class Temperature:
    """Represents a temperature."""

    def __init__(self, degrees=0):
        """Initialize temperature with specified degrees celsius.

        Args:
            degrees: number of degrees celsius
 
        """
        self.celsius = degrees

    def __str__(self):
        return f"{str(self.celsius)}°C"

    def __repr__(self):
        return f"Temperature({str(self.celsius)})"

    def comp(self, op, other):
        """Abstract out the value operations"""
        val = None
        if isinstance(other, Temperature):
            val = str(other.celsius)
        else:
            val = str(other)
        mv = str(self.celsius)
        expr = f"{mv} {op} {val}"
        return eval(expr)

    def mod(self, op, other):
        """Weeeee plus and minus abstraction"""
        val = None
        if isinstance(other, Temperature):
            val = str(other.celsius)
        else:
            val = str(other)
        expr = str(self.celsius) + " " + op + " " + val
        outp = eval(expr)
        self.celsius = outp
        return self

    def __eq__(self, other):
        return self.comp("==", other)

    def __gt__(self, other):
        return self.comp(">", other)

    def __lt__(self, other):
        return self.comp("<", other)

    def __le__(self, other):
        return self.comp("<=", other)

    def __ge__(self, other):
        return self.comp(">=", other)

    def __add__(self, other):
        return self.mod("+", other)

    def __sub__(self, other):
        return self.mod("-", other)
    
    def __hash__(self):
        return hash(str(self))



if __name__ == "__main__":
    normal = Temperature(20)
    hot = Temperature(100)

    if normal == 100:
        print("Something's wrong with =")
    else:
        print("= is fine")

    if normal > hot:
        print("Relative is wrong")

    if normal < hot:
        print("Relative is fine")

    print(sorted([Temperature(30), Temperature(45), Temperature(10), Temperature(20)]))

    if normal >= hot:
        print("Bad >= check")
    else:
        print("Good >= check")

    print(normal+5)
    print(hot-10)

    print("it's " + str(hot))

    hot -= 5

    print("it's now " + str(hot))


    boiling = Temperature(100)

    print("It's " + str(boiling))

    boiling += 10

    print("It's now " + str(boiling))

    print(hash(boiling))

    test = 5 + Temperature(5)

    print(test)