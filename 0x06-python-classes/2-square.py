#!/usr/bin/python3
"""define a class Square"""


class Square:
    """rep a class"""
    
    def __init__(self, size=0):
        """initializes the square
        Arg: 
            size(int): size of a side of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
