#!/usr/bin/python3
# 0-lookup.py
# Mark Oladeinde
"""Defines an object attribute lookup function.""",1


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
