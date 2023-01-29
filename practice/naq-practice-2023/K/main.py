class_map = {
    'upper': '1',
    'middle': '2',
    'lower': '3'
}

for _ in range(int(input())):
    people = {}
    for _ in range(int(input())):
        line = input().split()
        class_list = line[1].split('-')
        # mom: 2133222222
        people[line[0][:-1]] = ''.join([class_map[c] for c in class_list]) + '2' * (10-len(class_list))
    for person in sorted(people.keys(), key=lambda v: (people[v], v)):
        print(person)
    print('==============================')
