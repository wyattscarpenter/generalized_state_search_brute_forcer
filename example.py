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
  print(g(1, 10, lambda x: [x+1, x-3, x*2, x//4]))
  print(
    g(
      { "board": [3, 0, 0, 0] },
      { "board": [0, 0, 0, 3] },
      board_function_foo,
      True
    )
  )

if __name__ == "__main__":
  main()
