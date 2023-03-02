# Ali Abbas
import networkx as nx

path = "files/web-Google.txt" # Replace with your path to data
# File reading/handling
f = open(path, "r")

# Initialize graph using network x library
fullGraph = nx.read_edgelist(f, nodetype=int, create_using=nx.DiGraph, comments='#')

maxLabel = 0  # Largest Label in the Graph
largest_component = 0  # Length of The Largest Component
no_components = 0  # Number of Strong Connected Components

for node in fullGraph:
    if node > maxLabel:
        maxLabel = node


# Function for Depth First Search of a graph (Iterative)
def depth_first_search(n, visited, graph, count):
    dfs_stack = [n]
    while dfs_stack:
        item = dfs_stack.pop()
        if not visited[item]:
            count[0] += 1
            # print(f"{item} , ", end='')
            visited[item] = True

        for adj_node in sorted(graph.successors(item)):
            if not visited[adj_node]:
                dfs_stack.append(adj_node)


# Function to label nodes based on reach time (iterative)
def rhs(n, visited, graph, stack):
    chk_stack = [n]
    while chk_stack:
        item = chk_stack.pop()
        if not visited[item]:
            stack.append(item)
            visited[item] = True
        for adj_node in sorted(graph.successors(item)):
            if not visited[adj_node]:
                chk_stack.append(adj_node)


# Main Function for finding Strongly Connected Components
def find_scc():
    global largest_component
    global no_components

    stack = []    # stack of nodes based on reach time

    visited = [False] * (maxLabel + 1)

    for this_node in fullGraph:  # rhs on every non visited node
        if not visited[this_node]:
            rhs(this_node, visited, fullGraph, stack)

    transposed = fullGraph.reverse()        # Taking transpose of graph using networkx

    visited = [False] * (maxLabel + 1)
    counter = [0]

    while stack:
        curr = stack.pop()   # dfs traversal
        if not visited[curr]:
            no_components += 1
            counter[0] = 0
            depth_first_search(curr, visited, transposed, counter)
            if counter[0] > largest_component:
                largest_component = counter[0]


find_scc()  # Call for the main function

print("---------------------------------------")
print(f"No of Strong Connected Components = {no_components}")
print(f"Largest SSC Size = {largest_component}")
