from collections import defaultdict
from typing import List

import pytest


class Solution:
    """
    find all paths that include the directed edges listed in the tickets
    if all edges used:
        append path to list of paths
        return
    if edges from current node have been used
        return
    depth first search: starting from jfk
        for each child, call depth first search on the child, adding the edge between current -> child to our path
    join all airport names in itineraries and sort:
        sort: O(n log n) + n

    O(E * (E - V)) => E^2 - VE

    Optimal algorithm can achieve O(V) linear time
    this is essentially finding a euclidean path in a graph
    """

    def __init__(self):
        self.itineraries = []

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        flight_labels = defaultdict(list)
        for idx, (v1, v2) in enumerate(tickets):
            flight_labels[(v1, v2)].append(idx)
        for v1, v2 in tickets:
            adj_list[v1].append(v2)
        self.dfs("JFK", adj_list, flight_labels, len(tickets), [])
        joined_itineraries = []
        itineraries = []
        for flight_list in self.itineraries:
            flights = [tickets[flight_num] for flight_num in flight_list]
            itin = ["JFK"] + [dest for src, dest in flights]
            itineraries.append(itin)
            joined_itineraries.append("".join(itin))
        return sorted(zip(joined_itineraries, itineraries), key=lambda pair: pair[0])[0][1]

    def dfs(self, current, adj_list, flight_labels, num_flights, flights):
        if num_flights == 0:
            self.itineraries.append(flights)
            return
        can_fly_to = adj_list[current]
        for destination in can_fly_to:
            flight = (current, destination)
            flight_nums = flight_labels[flight]
            for flight_num in flight_nums:
                if flight_num not in flights:
                    self.dfs(destination, adj_list, flight_labels, num_flights - 1, flights + [flight_num])


@pytest.mark.parametrize('tickets, best_itinerary', [
    pytest.param([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], ["JFK", "MUC", "LHR", "SFO", "SJC"]),
    pytest.param([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
                 ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
    pytest.param(
        [["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], ["ANU", "EZE"], ["TIA", "ANU"], ["AXA", "TIA"],
         ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]],
        ['JFK', 'ANU', 'EZE', 'AXA', 'TIA', 'ANU', 'JFK', 'TIA', 'ANU', 'TIA', 'JFK'])
])
def test_find_itinerary(tickets, best_itinerary):
    solver = Solution()
    itinerary = solver.findItinerary(tickets)
    assert itinerary == best_itinerary
