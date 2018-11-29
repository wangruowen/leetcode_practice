# Determine whether a circular array of relative indices is composed of a single, complete cycle
def is_cycle(input):
    if len(input) == 0:
        return True

    visited = set()
    i = 0
    while i not in visited:
        visited.add(i)
        i = (i + input[i]) % len(input)
    return len(visited) == len(input)


input = [2,2,-1]  # True
input = [2,2,3]  # False
input = []  # True
input = [1,-1, 1234]
input = [1, 9, 0]
input = [2, -1, -1]
print(is_cycle(input))