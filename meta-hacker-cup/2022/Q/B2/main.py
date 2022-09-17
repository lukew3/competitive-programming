def solve(case_num):
    grid = []
    def isValidSpace(y, x):
        if grid[y][x] == '^':
            return True
        elif grid[y][x] == '#':
            return False
        else:
            # Recursive check
            tree_space_count = 0
            if y != 0: #N
                tree_space_count += isValidSpace(y-1, x)
            if x != c-1: #E
                tree_space_count += isValidSpace(y, x+1)
            if y != r-1: #S
                tree_space_count += isValidSpace(y+1, x)
            if x != 0: #W
                tree_space_count += isValidSpace(y, x-1)
            if tree_space_count < 2:
                return True
            else:
                return False

    r, c = map(int, input().split())
    if r != 1 and c != 1:
        # With rocks, just check that an existing tree has at least two neighboring spaces without rocks
        # Then fill in all non-rocks with trees
        for _ in range(r):
            grid.append(input())
        for y in range(r):
            for x in range(c):
                if grid[y][x] == '^':
                    tree_space_count = 0
                    # count tree_spaces
                    if y != 0: #N
                        tree_space_count += isValidSpace(y-1, x)
                    if x != c-1: #E
                        tree_space_count += isValidSpace(y, x+1)
                    if y != r-1: #S
                        tree_space_count += isValidSpace(y+1, x)
                    if x != 0: #W
                        tree_space_count += isValidSpace(y, x-1)
                    # check if not enough tree spaces 
                    if tree_space_count < 2:
                        print(f"Case #{case_num}: Impossible")
                        return
        print(f"Case #{case_num}: Possible")
        # print solution
        for row in grid:
            print(row.replace('.', '^'))
    else:
        # This half holds, even with rocks
        for i in range(r):
            grid.append(input())
            if '^' in grid[-1]:
                print(f"Case #{case_num}: Impossible")
                for _ in range(r-i-1):
                    input()
                return
        print(f"Case #{case_num}: Possible")
        for row in grid:
            print(row)

t = int(input())
for case in range(t):
    solve(case+1)
