"""
Given a unit measure conversion table, such as the following one:

1 yard -> 0.333 cm
1 yard -> 1.016 metric foot
1 yard -> 1 foot
1 mile -> x cm
...

and so on

Create a function that, given the above conversion table and a request input, such as:

2 yards

returns

0.666 cm

TODO :)
2 ways of solving it:

1. graph and bfs
2. I think union find would also do the trick here

In the end, what you care about is connected components, this is, understanding whether u can get
from measure X to measure Y via a path <--> iff they belong to the same disjoint set
"""

import re
from collections import defaultdict, deque

METRIC_MATCHER = re.compile("(\d)( )(.*)")
REQUESTER_MATMCHER = re.compile("(\d) (.*) to (.*)")


def measure_converter(table: dict[str, str], request: str) -> str:
    def converter(base_unit_from: float, base_unit_to: float, to_measure: str,
                  val: float) -> str:
        return f'{(val * base_unit_to) / base_unit_from} {to_measure}'

    measures_graph = defaultdict(list)

    # build graph
    for from_measure, to_measure in table.items():
        base_unit_from, _, measure_from = METRIC_MATCHER.findall(from_measure)[0]
        base_unit_to, _, measure_to = METRIC_MATCHER.findall(to_measure)[0]

        measures_graph[measure_from].append((base_unit_from, base_unit_to, measure_to))

    val, from_measure, to_measure = REQUESTER_MATMCHER.findall(request)[0]

    print(measures_graph)

    # solution 1: BFS
    visited = set()

    tovisit = deque()
    tovisit.append(from_measure)
    found = False
    while len(tovisit) > 0:
        curr = tovisit.popleft()
        visited.add(curr)
        if curr == to_measure:
            found = True
            break  # we have reached the measure we want!
        for measure_neighbor in measures_graph[curr]:
            if measure_neighbor not in visited:
                tovisit.append(measure_neighbor)
       
    if not found:
        raise ValueError(f"Cannot convert {from_measure} to {to_measure} from the information in the table")
    else:
        val, from_measure, to_measure = REQUESTER_MATMCHER.findall(request)[0]
        measure_neighbors = measures_graph[from_measure]
        for base_unit_from, base_unit_to, measure_neighbor in measure_neighbors:
            if measure_neighbor == to_measure:
                return converter(base_unit_from, base_unit_to, to_measure, val)
        # TODO: build path

    # solution 2: UF


example = {
    "1 metric foot": "1 inch",
    "1 metric foot": "0.333 cm",
    "0.38 metric foot": "1 crazy unit",
    "1 yard": "0.123 miles",
    "1 cm": "0.12 sht",
}

assert "0.36 sht" == measure_converter(example, "3 cm to sht")
