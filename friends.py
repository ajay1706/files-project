# Asks the user for the list of 3 friends
#  For each friend, will tell the user whether they are nearby
# For each friend we'll save the friend to  'nearby_friends.txt'
# hint: readLines()

friends = input('Enter your 3 friends list separated by comma:').split(',')

people = open('people.txt','r')
people_nearby = [line.strip() for line in people.readlines()]
people.close()


friends_set = set(friends)

people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby, meetup')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()