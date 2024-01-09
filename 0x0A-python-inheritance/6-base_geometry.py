#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represents basegeometry with exception"""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
