users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    userName = user["name"]
    userId = user["id"]
    numFriends = 0
    
    for link in friendship:
        if link[0] == userId:
            numFriends += 1
    return numFriends

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    sortedList = []
    for user in users:
        sortedList.append((user["name"], num_friends(user)))
    sortedList.sort(key=lambda tup: tup[1], reverse=True)
    print(sortedList)
    
print(users[0]['name'], "has", num_friends(users[0]), "friends")
print(users[2]['name'], "has", num_friends(users[2]), "friends")
print(users[9]['name'], "has", num_friends(users[9]), "friends")
sort_by_num_friends()