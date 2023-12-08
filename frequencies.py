"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in items:
        string = str(i)
        if string in frequencies:
            frequencies[string] += 1
        else:
            frequencies[string] = 1
    return frequencies
