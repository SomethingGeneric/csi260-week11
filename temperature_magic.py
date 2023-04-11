"""An object representation for working with temperatures.

Author: Matt Compton
Class: CSI-260-01
Assignment: Week 11 Lab
Due Date: April 10, 2023 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""


class Temperature:
    """Represents a temperature."""

    def __init__(self, degrees=0):
        """Initialize temperature with specified degrees celsius."""
        self.celsius = degrees

    def __str__(self):
        """String representation of self."""
        return f"{str(self.celsius)}°C"

    def __repr__(self):
        """Representation of self is always a string, sorry."""
        return f"Temperature({str(self.celsius)})"

    def comp(self, op, other):
        """Abstract out the value operations."""
        val = None
        if isinstance(other, Temperature):
            val = str(other.celsius)
        else:
            val = str(other)
        mv = str(self.celsius)
        expr = f"{mv} {op} {val}"
        return eval(expr)

    def mod(self, op, other, i=False, r=False):
        """Abstraction for any value modification dunder methods."""
        val = None
        if isinstance(other, Temperature):
            val = str(other.celsius)
        else:
            val = str(other)
        if not r:
            expr = str(self.celsius) + " " + op + " " + val
        else:
            expr = val + " " + op + " " + str(self.celsius)
        print("MOD: " + expr)
        outp = eval(expr)
        if i:
            self.celsius = outp
            return self
        else:
            return Temperature(outp)

    def __eq__(self, other):
        """Comparison dunder method."""
        return self.comp("==", other)

    def __gt__(self, other):
        """Greather than dunder method."""
        return self.comp(">", other)

    def __lt__(self, other):
        """Less than dunder method."""
        return self.comp("<", other)

    def __le__(self, other):
        """Less than or equals dunder."""
        return self.comp("<=", other)

    def __ge__(self, other):
        """Greater or equal dunder."""
        return self.comp(">=", other)

    def __add__(self, other):
        """Add dunder method."""
        return self.mod("+", other)
   
    def __radd__(self, other):
        """Right hand add dunder method"""
        return self.mod("+", other)
   
    def __iadd__(self, other):
        """In-place add method"""
        return self.mod("+", other, True)

    def __sub__(self, other):
        """Subtract dunder"""
        return self.mod("-", other)
    
    def __rsub__(self, other):
        """Right hand sub dunder"""
        return self.mod("-", other, False, True)
    
    def __isub__(self, other):
        """In-place sub method"""
        return self.mod("-", other, True)
    
    def __hash__(self):
        """Dict key hash method"""
        return hash(str(self))