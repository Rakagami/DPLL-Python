# DPLL-Python

A CLI tool to try out a DPLL implementation. See [this](https://en.m.wikipedia.org/wiki/DPLL_algorithm) for more information.

## Getting Started

This is just a simple python script. I added a shebang for python3 if it's installed in `/usr/bin/python3` for my convenience. But anyone should be able to use it by executing the script with python3.

## How to use

Type in `python DPLL.py [Literal1] [Literal2] [Literal3]...` to execute the python script

Literalsyntax:
Variable in Negation are uppercase characters, otherwise it's lowercase.

Example:
The Literal `{{¬s,¬q},{q, r,¬p,¬s}}` would be represented as `SQ qrPS` so in the CLI it would look like this: ```python3 ./DPLL.py SQ qrPS```

Executing this command would give you this output:

```
> python3 DPLL.py SQ qrPS
> ['p', 'q', 'r', 's']
> [1, 1, -1, 0]
>
```

The first line is the list of variables represented as characters. The second line is a possible interpretation for it. If no output is given, no interpretation is possible. -1 means that it doesn't matter whether it is 0 or 1.

### Prerequisites

To execute the script you need to have python3 installed.

## Authors

* **Prakita Renatin** - *Github:* - [Rakagami](https://github.com/Rakagami)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Guidelines for the implementation is taken out if Discrete Structures script from TU Munich.
