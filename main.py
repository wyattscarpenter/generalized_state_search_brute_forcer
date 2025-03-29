#!/usr/bin/env python3

"""Hi, welcome to the readme, which is just symlinked to the main.py file.
This is Wyatt S Carpenter's generalized state search brute forcer, a program which implements a common pattern I've often seen and need.
Given a set of rules (lambdas), an initial state, and a desired state, this program uses a breadth-first search on the state space to find a solution (also: guaranteed to be one of the shortest solutions, funny enough!
(COULD: one day give it a "cost function" as well, and minimize that instead of steps. But hey. Why bother?).
This program uses a brute-force method and also is written in Python, so I hope you have a lot of RAM, and a lot of time on your hands!
This program requires Python 3.12 or later, but purely in order to use the Type Parameter Syntax (the def foo[T]() type thing). You can just scrape that syntax off if you want to use it in earlier pythons.
"""

from sys import argv

def generalized_state_search_brute_forcer[S1, S2](initial_state: S1, desired_state: S2, rules: Callable[[S1], S2], print_debug_information: bool = False) -> []:
  """This function searches state space starting from initial_state until it finds desired_state. May take a while.
  Note that the types S1 and S2 (meant to stand for State, and representing whatever type you bring to the table for that, like a dict or whatever) almost certainly have to be the same. If they're different, you can only have a chain of states 1 link long! But I've left in that edge case out of perversity."""

if __name__ == "__main__":
  print(f"{argv[0]} has no main funciton, because it is a library and not a script. Try importing it and then using your ")