class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.name}"

    def __eq__(self, other):
        return self.name == other.name


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    directions = lines[0].strip()
    nodes = {}

    for line in lines[2:]:
        start, paths = line.strip().split(" = ")
        paths = paths.replace("(", "").replace(")", "")
        left, right = paths.split(", ")

        # Check if nodes exist in the dictionary, if not, create them
        if start not in nodes:
            nodes[start] = Node(start)
        if left not in nodes:
            nodes[left] = Node(left)
        if right not in nodes:
            nodes[right] = Node(right)

        # Connect nodes
        nodes[start].add_child(nodes[left])
        nodes[start].add_child(nodes[right])

    start = nodes["AAA"]
    target = nodes["ZZZ"]

    print(f"Steps: {get_steps(start, target, directions)}")


def get_steps(start, target, directions):
    steps = 0
    current = start
    while current != target:
        print(f"Current: {current} -> {current.children}")
        direction = directions[steps % len(directions)]
        if direction == "R" and current.children:
            current = current.children[1]
        elif direction == "L" and current.children:
            current = current.children[0]
        steps += 1
    return steps


if __name__ == '__main__':
    main()
