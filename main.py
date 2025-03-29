#!/usr/bin/env python3

"""Hi, welcome to the readme, which is just symlinked to the main.py file.
This is Wyatt S Carpenter's generalized state search brute forcer, a program which implements a common pattern I've often seen and need.
Given a set of rules (lambdas), an initial state, and a desired state, this program uses a breadth-first search on the state space to find a solution (also: guaranteed to be one of the shortest solutions, funny enough!
(COULD: one day give it a "cost function" as well, and minimize that instead of steps. But hey. Why bother?).
This program uses a brute-force method and also is written in Python, so I hope you have a lot of RAM, and a lot of time on your hands!
This program requires Python 3.12 or later, but purely in order to use the Type Parameter Syntax (the def foo[T]() type thing). You can just scrape that syntax off if you want to use it in earlier pythons.
"""

from sys import argv
# from collections.abc import Callable # do I need this?

def generalized_state_search_brute_forcer[S](initial_state: S, desired_state: S, production_rules: Callable[[S], S], print_debug_information: bool = False) -> list[S]:
  """This function searches state space starting from initial_state until it finds desired_state. May take a while.
  Return value is a list of states from initial to desired. No information about which rules were used is returned. (COULD: extend the program to do so.)
  The type S is meant to stand for State, and represents whatever type you bring to the table for that, like a dict or whatever."""
  all_states: set = set(initial_state) # set insertion order is conserved in python (I think?) so this set can also function as a queue (I think?)
  reversewalkable_links = dict()
  while True:
    for s in all_states:
      for r in production_rules:
        result = r(s)
        if result == desired_state:
          # we win...
        else:
          reversewalkable_links.add(result, s)
          all_states.insert()
  return array_of_states
if __name__ == "__main__":
  print(f"{argv[0]} has no main funciton, because it is a library and not a script. Try importing it and then using your ")