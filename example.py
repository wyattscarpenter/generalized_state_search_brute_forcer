#!/usr/bin/env python3

"""Small example program for demonstrating generalized_state_search_brute_forcer."""

from main import generalized_state_search_brute_forcer as g

def board_function_foo(board):
  b = board["board"]
  return [
    { "board": [b[0], b[1], b[2], b[3]] },
    { "board": [b[1], b[0], b[2], b[3]] },
    { "board": [b[0], b[2], b[1], b[3]] },
    { "board": [b[0], b[1], b[3], b[2]] },
  ]

def main():
  print("Hello from example!")
  print(number_result := g(1, 10, lambda x: [x+1, x-3, x*2, x//4]))
  assert(number_result==[1, 2, 4, 5, 10]) # I haven't personally checked if this is right, but it is the result I got, and it looks ok.
  print(
    moving_result := g(
      { "board": [3, 0, 0, 0] },
      { "board": [0, 0, 0, 3] },
      board_function_foo,
      print_debug_information=True
    )
  )
  assert(moving_result==[{'board': [3, 0, 0, 0]}, {'board': [0, 3, 0, 0]}, {'board': [0, 0, 3, 0]}, {'board': [0, 0, 0, 3]}])

if __name__ == "__main__":
  main()
