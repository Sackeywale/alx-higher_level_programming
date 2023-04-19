#!/usr/bin/python3
"""define a class Square"""


class Square:
    """rep a class"""
    
    def __init__(self, size=0):
        """initializes the square
        Arg: 
            size(int): size of a side of the square
        Raises:
            TypeError: when size is not integer
            ValueError: when size is < 0
        """
        
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")

        self.__size = size
