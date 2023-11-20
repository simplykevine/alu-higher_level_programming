#!/usr/bin/python3
"""Square class defination"""


class Square:
    """Square class body"""

    def __init__(self, size=0, position=(0, 0)):
        """Square constructor .
        Args:
            size (int): The size of the new square.
            square position (int, int): of Tupple.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Setter and getter of a  square."""
        return (self.__size)
