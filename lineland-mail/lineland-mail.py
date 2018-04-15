# coding: utf-8
# Author: Júlia Fernandes Alves <juliafealves@gmail.com>
# Handle: juliafealves - A. Lineland Mail
from math import sqrt


# Distance between two points.
def distance(point_a, point_b):
    return sqrt((point_a - point_b) ** 2)


number_cities = int(raw_input())
cities = map(int, raw_input().split())

for i in xrange(number_cities):
    if i == 0:
        min_cost = distance(cities[i], cities[i + 1])
        max_cost = distance(cities[i], cities[-1])
    elif i == len(cities) - 1:
        min_cost = distance(cities[i], cities[i - 1])
        max_cost = distance(cities[i], cities[0])
    else:
        min_cost = min(distance(cities[i], cities[i + 1]), distance(cities[i], cities[i - 1]))
        max_cost = max(distance(cities[i], cities[0]), distance(cities[i], cities[-1]))

    print '%i %i' % (min_cost, max_cost)



