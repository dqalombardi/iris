# Python package `iris`

## Description

Package containing utilities for printing to stdout in color.

## Examples

```python
from iris import cprint, ANSIColor

cprint("Hello, World!", color=ANSIColor.CYAN)
```

```python
from iris import colored, ANSIColor

prompt = colored("What is your name?\n> ", color=ANSIColor.YELLOW)
user_name = input(prompt)
cprint(f"Nice to meet you, {user_name}!", color=ANSIColor.PURPLE)
```

```python
from iris import cprint, ANSIColor

cprint(
    "first",
    "second",
    "third",
    sep="\n",
    color=ANSIColor.GREEN,
)
```
