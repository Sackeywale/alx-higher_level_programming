#!/usr/bin/python3
"""Rectangle that define a rectangle
"""

class Rectangle:
    """class Rectangle that defines a rectangle
    """
    def __init__(self, width, height):
        """Initialize the rectangle
        args: 
            width: smallest side of the rectangle
            height: biggest side of the rectange
        raises:
            TypeError: must be an integer
            ValueError: must be >= 0
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """to retrieve the it"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """to set it"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """to retrieve it"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """to set it"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")

        self.__height = value
