"""Tools for working with Temperatures."""


class Temperature:
    """Represents a temperature."""

    def __init__(self, degrees=0):
        """Initialize temperature with specified degrees celsius.

        Args:
            degrees: number of degrees celsius
 
        """
        self.celsius = degrees
