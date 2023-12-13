#!/usr/bin/python3
"""Defines the attribute of an object in function lookup"""

def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return (dir(obj))
