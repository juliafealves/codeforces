# coding: utf-8
# Author: Júlia Fernandes Alves <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: A. Game With Sticks https://bit.ly/2HaIWBT

PLAYER_0 = 'Akshat'
PLAYER_1 = 'Malvika'

grid = map(int, raw_input().split())
smaller = min(grid)

if smaller % 2 == 0:
    print PLAYER_1
else:
    print PLAYER_0
