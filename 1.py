class graf:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


start = graf("Animals")

b = graf("Mammals")
c = graf("Birds")
d = graf("Fishes")

e = graf("Dog")
f = graf("Cat")

g = graf("Tuna")
h = graf("Salmon")
i = graf("Carp")

j = graf("Sparrow")
k = graf("Pigeon")
l = graf("Peacock")

start.add_child(b)
start.add_child(c)
start.add_child(d)

b.add_child(e)
b.add_child(f)

c.add_child(j)
c.add_child(k)
c.add_child(l)

d.add_child(g)
d.add_child(h)
d.add_child(i)


Adjacency_List = []

def build_adjacency_list(node):
    for child in node.children:
        Adjacency_List.append([node.value, child.value])
        build_adjacency_list(child)

build_adjacency_list(start)

print("Adjacency List:")
for parent, child in Adjacency_List:
    print(f"{parent} => {child}")



Materialized_Path = []

def build_materialized_path(node, parent_path=""):
    current_path = node.value if parent_path == "" else parent_path + "/" + node.value
    Materialized_Path.append([node.value, current_path])

    for child in node.children:
        build_materialized_path(child, current_path)

build_materialized_path(start)

print("\nMaterialized Path:")
for node, path in Materialized_Path:
    print(path)


# конвертация из Adjacency List в Materialized Path

def adjacency_to_materialized(adjacency_list):
    tree = {}
    children = set()

    for parent, child in adjacency_list:
        tree.setdefault(parent, []).append(child)
        children.add(child)

    root = None
    for parent in tree:
        if parent not in children:
            root = parent
            break

    result = []

    def dfs(node, path):
        result.append([node, path])
        for child in tree.get(node, []):
            dfs(child, path + "/" + child)

    dfs(root, root)
    return result


# конвертация из Materialized Path в Adjacency List

def materialized_to_adjacency(materialized_path):
    adjacency = set()

    for node, path in materialized_path:
        parts = path.split("/")
        for i in range(len(parts) - 1):
            adjacency.add((parts[i], parts[i + 1]))

    return list(adjacency)



print("\nConverted Materialized Path (from Adjacency List):")
converted_mp = adjacency_to_materialized(Adjacency_List)
for node, path in converted_mp:
    print(path)

print("\nConverted Adjacency List (from Materialized Path):")
converted_adj = materialized_to_adjacency(Materialized_Path)
for parent, child in converted_adj:
    print(f"{parent} => {child}")