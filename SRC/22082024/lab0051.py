#continue statement
"""
   continue statement skips the current loop and
   move to the next iteration.

i | condition | O/P
0 | 0%2 ==0 -> true |continue-- Skip no O/P
1 | 1%2 ==0 -> false |1
2 | 2%2 ==0 -> true |continue-- Skip no O/P
3 | 3%2 ==0 -> false |3

"""

for n in range(10):
    if n % 2 == 0:
        continue
    print(n)

# pass -- can be used in the statment, functions, class and objects 