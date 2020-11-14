class GraphNode:
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph:
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1: GraphNode, node2: GraphNode):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)
    
    def remove_edge(self, node1: GraphNode, node2: GraphNode):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)

nodeG = GraphNode("G")
nodeR = GraphNode("R")
nodeA = GraphNode("A")
nodeP = GraphNode("P")
nodeH = GraphNode("H")
nodeS = GraphNode("S")

graph1: Graph = Graph([nodeG, nodeR, nodeA, nodeP, nodeH, nodeS])
graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)

def update_frontier(node: GraphNode, explored_set, frontier):
    for i in node.children:
        if i.value not in explored_set:
            frontier.append(i)

def bfs_search(root_node: GraphNode, search_value):
    if root_node.value == search_value:
        return root_node

    frontier = []
    explored_set = set()
    explored_set.add(root_node.value)
    update_frontier(root_node, explored_set, frontier)

    while len(frontier) > 0:
        node: GraphNode = frontier.pop(0)
        if node.value == search_value:
            return node
        explored_set.add(node.value)
        update_frontier(node, explored_set, frontier)

print(bfs_search(nodeS, "A"))
print(bfs_search(nodeP, "S"))
print(bfs_search(nodeH, "R"))
print(nodeA)
print(nodeS)
print(nodeR)
    