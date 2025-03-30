#!/usr/bin/env python3

"""This file solves the levels of Dicey Dungeons Halloween 2021 Witch Episode using generalized_state_search_brute_forcer, as a more-complicated example.
See https://www.youtube.com/watch?v=9sIevBVlC78 for a video of the game in action."""

from main import generalized_state_search_brute_forcer as g

DEBUG = False #True # feel free to set this to true or false as you desire

def dprint(*args, **kwargs):
  if DEBUG:
    print(*args, **kwargs)

def compute_buyable_spells(dice: dict[int, int], spellbook: dict[int,int]) -> list[tuple[int, int]]:
  """Return the buyable spells, and also the quantity you need to use to buy said spell."""
  return [(pips, quantity) for pips, quantity in dice.items() if (pips in spellbook) and (quantity >= spellbook[pips])]

def witch_every_level(s):
  """Place spells on empty slot according to their cost. We rely on the fact that order doesn't matter, and always take the first empty slot."""
  buyable_spells = compute_buyable_spells(s["dice"], s["spellbook"])
  dprint(s["dice"], s["spellbook"], buyable_spells)
  board = s["board"]
  possible_new_states = []
  for i, slot in enumerate(s["board"]): #this basically just exists to find the first 0, which we always take. Remember, we're just providing more states, so the next action can also be a buy.
    dprint(slot)
    if slot == 0:
      for bs in buyable_spells:
        possible_new_board_info = board[:i]+[bs[0]] + board[i+1:]
        dprint(possible_new_board_info)
        new_possible_state = s.copy()
        new_possible_state["board"] = possible_new_board_info
        d = s["dice"].copy()
        print(d, bs)
        d[bs[0]] -= bs[1]
        print(d, bs)
        new_possible_state["dice"] = d
        possible_new_states.append(new_possible_state)
      break # order doesn't matter, so we just break to go to the return here (otherwise we would invalidly buy things we couldn't afford)
  return possible_new_states

def witch_level_1(s):
  #TODO
  s
  return witch_every_level(s)

def main():
  print("Hello from witch!")
  # I didn't label this anywhere, but the spellbook just contains (spell number: cost) mappings (each spell of (spell number) costs (cost) (spell number) dice . The spell behaviors are fully within the production rule function.
  # dice is (spell number: quantity). This eliminates some busywork elsewhere (invoking counter to get this form, if dice were natively a list, say). 
  print(
    g(
      { "board": [3, 0, 0, 0], "dice": {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}, "spellbook": {1: 1, 2: 2, 3: 1}, "damage": 0 },
      {},
      witch_level_1,
      desire_function=lambda b: b["damage"] >= 10,
      print_debug_information=True
    )
  )

if __name__ == "__main__":
  main()
