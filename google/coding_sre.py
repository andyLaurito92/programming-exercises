"""
"We have a system that logs events, where each event is tagged with a timestamp (in seconds)
and a userID. Given a list of these events, I want you to design and implement
a function that, given a time window (startTime, endTime), returns the top k
users who generated the most events in that time window."

Follow-up details:

- The list of events is unsorted and can be very large (millions of events).
- Time complexity and memory efficiency are important.
- k is much smaller than the total number of users.
- You can assume the input is a list of (timestamp, userID) pairs, and the window is [startTime, endTime] (inclusive).
"""


"""
1M -> 1*10^6
userid -> 50 B
timestamp -> 100 B
150 B * 1*10^6 = 15 * 10^7 B

1 GB -> 2^30 B

15 * 10^7 B / 2^30 -> 0,1396983862 GB
"""


userid = str
timestamp = int 

from collections import defaultdict
from operator import itemgetter
import heapq


def topkusers(events: list[(timestamp, userid)], time_window:(timestamp, timestamp), k:int) -> list[userid]:
    start, end = time_window

    events_per_user = defaultdict(int)
    heap = []

    for eventtime, userid in events:
        if eventtime > end or eventtime < start:
            continue

        events_per_user[userid] += 1
        heappop(heap, (userid, 

    res = list(events_per_user.items())
    res.sort(key=itemgetter(1), reverse=True)
    return list(map(itemgetter(0), res[:k]))



events = [
    (1622505600, 'user1'),  # 2021-06-01 00:00:00 UTC
    (1622509200, 'user2'),  # 2021-06-01 01:00:00 UTC
    (1622512800, 'user1'),  # 2021-06-01 02:00:00 UTC
    (1622516400, 'user3'),  # 2021-06-01 03:00:00 UTC
    (1622520000, 'user1'),  # 2021-06-01 04:00:00 UTC
    (1622523600, 'user2'),  # 2021-06-01 05:00:00 UTC
    (1622527200, 'user3'),  # 2021-06-01 06:00:00 UTC
    (1622530800, 'user2'),  # 2021-06-01 07:00:00 UTC
]

start = 1622505600 # (2021-06-01 00:00:00 UTC)
end = 1622520000 # (2021-06-01 04:00:00 UTC)

assert ["user1", "user2"] == topkusers(events, (start, end), 2)
