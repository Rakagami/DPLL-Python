# DPLL-Python
Basic DPLL implementation in Python. Guidelines for the implementation is taken out if Discrete Structures script from TU Munich.
For testing python 2.7.15 was used

# How to use
type in ```python DPLL.py [Literal1] [Literal2] [Literal3]...``` to execute the python script

Literalsyntax:
Variable in Negation are uppercase characters, otherwise it's lowercase.

Example:
```{{¬s,¬q},{q, r,¬p,¬s}} => SQ qrPS``` so in the CLI it would look like this: ```python DPLL.py SQ qrPS```

# TODO
- OLR and PLR integration
- Visual representation of the tree
