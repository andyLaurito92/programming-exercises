"""
List of Users with UserId and Name
List of Logins with UserId and timestamp
Return leaderboard - Name and unique(login),

Example:
Users - [{1,"qw"},{2,"er"}]
Logins - [{1,1},{1,1},{1,3},{2,4},{2,5},{1,7}]
output (Print in descending order based on login attempts)
"qw" : 3
"er" : 2

User "qw" logged 4 times in total, unique attempts - 3. you can assume any input type (either 2d array or List).
"""

from operator import itemgetter

users = [{1,"qw"},{2,"er"}] # (id, name)
logins = [{1,1},{1,1},{1,3},{2,4},{2,5},{1,7}]  # (id, timestamp)



def leaderbord(users, logins) -> list[(str, int)]:
    """
    Given a list of users and logins, returns the
    user that most login into the system

    N = len(users)
    M = len(logins)

    Complexity: O(M + N*log N) # iterating over logins + sorting by login count
    Memory: O(N)
    """
    users_dict = {userid: name for userid, name in users}
    login_count = {}
    for userid, name in users:
        login_count[userid] = 0

    userid_max_login = users[0][0] # initialize max_login in first user
    for userid, login_time in logins:
        login_count[userid] += 1
        if userid != userid_max_login and login_count[userid] > login_count[userid_max_login]:
            userid_max_login = login_count[userid]
    userid_logins = list(login_count.items())
    userid_logins.sort(key=itemgetter(1), reverse=True)
    return [(users_dict[userid], count) for userid, count in userid_logins]


users = [(1,"qw") , (2,"er")] # (id, name)
logins = [(1,1), (1,1), (1,3), (2,4), (2,5), (1,7)]  # (id, timestamp)

assert leaderbord(users, logins) == [("qw", 4), ("er", 2)]
