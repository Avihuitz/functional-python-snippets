"""
Functional Python Snippets Collection
=====================================

A personal collection of functional programming exercises written in Python.  
These examples use closures, dispatch dictionaries, and lambda logic to 
simulate object-like behavior — all without classes.

Modules included:
-----------------
1. power.py      - Immutable ADT for base and exponent operations
2. make_tree.py  - Functional binary tree with depth, balance, BST validation
3. coding.py     - Simple cipher system with word/letter reversal and Caesar shift
4. parking.py    - Simulated parking system using closures to manage state
5. pricing.py    - Discount calculator using functional patterns (map/reduce)

Design philosophy:
------------------
• No OOP. Everything is done using functions, stateful closures, and message-passing.  
• Functions return other functions (or dispatch dictionaries) as APIs.  
• Emphasis on readability and logic over optimization.  

Examples:
---------
# Power ADT
- x = make_power(2, 3)
- print_power(x)        # 2^3
- calc_power(x)         # 8

# Cipher
- c = coding()
- c("set_key", (3, "yes", "no"))
- secret = c("encoding", "hello world")
- c("decoding", secret)

# Tree
- t = make_tree(4, make_tree(2), make_tree(6))
- tree_BST(t)           # True
- tree_depth(t)         # 1

# Parking
- park = parking(10, 2, 2, 1)
- park["start_parking"](123, "VIP")
- park["print_parking"]("VIP")

Notes:
------
Written as part of a self-study practice project, this repo shows how far
closures and higher-order functions can be stretched to mimic structure.
"""
