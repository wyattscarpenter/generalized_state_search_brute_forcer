#!/usr/bin/env python3

"""Hi, welcome to the readme, which is just symlinked to the main.py file.
This is Wyatt S Carpenter's generalized state search brute forcer, a program which implements a common pattern I've often seen and need.
Given a production rule, an initial state, and a desired state, this program uses a breadth-first search on the state space to find a solution (also: guaranteed to be one of the shortest solutions, funny enough!
(COULD: one day give it a "cost function" as well, and minimize that instead of steps. But hey. Why bother?).
This program uses a brute-force method and also is written in Python, so I hope you have a lot of RAM, and a lot of time on your hands!
This program requires Python 3.12 or later, but purely in order to use the Type Parameter Syntax (the def foo[T]() type thing). You can just scrape that syntax off if you want to use it in earlier pythons.
"""

from sys import argv
from collections.abc import Callable, Iterable

def generalized_state_search_brute_forcer[S](initial_state: S, desired_state: S, production_rule: Callable[[S], Iterable[S]], print_debug_information: bool = False) -> list[S]|None:
  """This function searches state space starting from initial_state until it finds desired_state. May take a while.
  Return value is a list of states from initial to desired. No information about which rules were used is returned. (COULD: extend the program to do so.)
  The type S is meant to stand for State, and represents whatever type you bring to the table for that, like a dict or whatever. S *must* be hashable, except that for common builtin unhashable datatypes (dict, set, list) I've already built-in a workaround, so you can just use those anyway.
  The production rule should be one function that, given a state, returns all the possible resulting states. For instance, all the possible states of a chess board after a move is made in the current state.
  Hot tip: you can prevent the production rule from emitting invalid states entirely OR just make all invalid states map to an error value, like {"I am error"} that can never make it to the desired state. It's all the same to the program."""

  def dprint(*args, **kwargs):
    if print_debug_information:
      print(*args, **kwargs)

  def make_hashable(x: object):
    "The best way to set up the state tracking is something like a dict or set. But unfortunately that runs into the issue that dicts need to be able to hash their keys ie their keys can't be dicts. What a bad programming language!"
    if isinstance(x, dict):
      return tuple((make_hashable(k), make_hashable(v)) for k, v in sorted(x.items()))
    elif isinstance(x, set):
      return tuple(sorted(x))
    elif isinstance(x, list):
      return tuple(x)
    else:
      return x

  seen_states = set() # Keeping this around is just an optimization over checking `x in states_queue` each time. (Which optimization I have not tested.)
  states_queue: list[S] = [initial_state] # how do you write a queue in python? Probably just a list, right? We also append to this during the loop (and never remove from the front — why bother!)
  reversewalkable_links = dict()
  for s in states_queue:
    dprint(f"Considering state {s}:")
    for result in production_rule(s):
      dprint(f"Considering result {result}:")
      hashable_result = make_hashable(result)
      dprint(f"{hashable_result=}")
      if result == desired_state:
        dprint("We win... so collect and return the state steps.")
        state_steps = [result, s]
        while (ss := state_steps[-1]) != initial_state:
          state_steps.append(reversewalkable_links[make_hashable(ss)])
        return list(reversed(state_steps))
      if hashable_result in seen_states:
        dprint("Already seen.")
        continue
      else:
        dprint("Not already seen. Adding to collection...")
        seen_states.add(hashable_result)
        reversewalkable_links[hashable_result] = s
        states_queue.append(result)
  return None

if __name__ == "__main__":
  print(f"{argv[0]} has no main funciton, because it is a library and not a script. Try importing it and then using it.")
