# Python: Deadlock Detection Algorithm

# Input:
# Numbers of nodes: 13
# Node names: R A C S D T B E F U V W G
# Edges:
# R to A
# A to S
# C to S
# F to S
# W to S
# D to S
# U to D
# G to U
# D to T
# B to T
# T to E
# E to V
# V to G

# graph_dict = {'R': ['A'], 'A': ['S'], 'S': [], 'C': ['S'], 'F': ['S'], 'W': ['S'], 'D': [
#     'S', 'T'], 'U': ['D'], 'G': ['U'], 'T': ['E'], 'B': ['T'], 'E': ['V'], 'V': ['G']}


graph_dict = {}
total_nodes = int(input("Number of nodes: "))
nodes_names = input("Note names: ").split(" ")

for _ in range(total_nodes):
    edges = input("Edges: ").split(" ")
    if edges[0] not in graph_dict:
        graph_dict[edges[0]] = []
    if edges[2] not in graph_dict:
        graph_dict[edges[2]] = []
    graph_dict[edges[0]].append(edges[2])


def node_counter(node, depth):
    cnt = 0
    for n in depth:
        if node == n:
            cnt += 1
    return cnt


def node_depth(curr_node, curr_next_node, depth=[]):
    while True:
        depth.append(curr_node)
        if not graph_dict[curr_next_node]:
            return depth

        curr_node = curr_next_node
        curr_next_node = graph_dict[curr_next_node][0]


is_terminate = False
for node, next in graph_dict.items():
    if is_terminate:
        break
    if not next:
        continue

    for next_node in next:
        depth = node_depth(node, next_node, depth=[])
        if node_counter(node, depth) == 2:
            print("Deadlock Cycle: ", depth)
