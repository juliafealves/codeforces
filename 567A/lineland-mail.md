# A. Lineland Mail
All cities of Lineland are located on the *Ox* coordinate axis. Thus, each city is associated with its position `xi — a` 
coordinate on the *Ox* axis. No two cities are located at a single point.

Lineland residents love to send letters to each other. A person may send a letter only if the recipient lives in another 
city (because if they live in the same city, then it is easier to drop in).

Strange but true, the cost of sending the letter is exactly equal to the distance between the sender's city and the 
recipient's city.

For each city calculate two values ​​*mini* and *maxi*, where mini is the minimum cost of sending a letter from the *i*-th city 
to some other city, and *maxi* is the the maximum cost of sending a letter from the *i*-th city to some other city

### Input
The first line of the input contains integer `n (2 ≤ n ≤ 10ˆ5)` — the number of cities in Lineland. The second line 
contains the sequence of `n` distinct integers `x1, x2, ..., xn ( - 10ˆ9 ≤ xi ≤ 109)`, where *x i* is the x-coordinate of
the *i*-th city. All the *x i*'s are distinct and follow in **ascending** order.

### Output
Print `n` lines, the *i*-th line must contain two integers *min i*, *max i*, separated by a space, where *min i* is the 
minimum cost of sending a letter from the *i*-th city, and *max i* is the maximum cost of sending a letter from the 
*i*-th city.

### Examples
```
# input
4
-5 -2 2 7
# output
3 12
3 9
4 7
5 12

# input
2
-1 1
# output
2 2
2 2
```