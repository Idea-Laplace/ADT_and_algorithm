"""
R-2.20
What are some potential efficiency disadvantage of having very deep
inheritance trees, that is, a large set of classes, A, B, C, and so on,
such that B extends A, C extends B, D extends C, etc?
"""

"""
The structure of whole classes from root to leaf
is of onion-like, calling unnecessary chain of intermdiary classes.
"""