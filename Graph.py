from queue import Queue
from stack import Stack


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()  # this will hold edges

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:

            self.vertices[v1].add(v2)  # there's an edge from v1 to v2
        else:
            raise IndexError("nonexistent vert")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()
        # Create a set to store the visited nodes
        visited = set()

        # Init: enqueue the starting node
        q.enqueue(starting_vertex_id)

        # While the queue isn't empty
        while q.size() > 0:

            # Dequeue the first item
            v = q.dequeue()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)

                # Do something with the node
                print(f"Visited {v}")
                # Add all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)


g = Graph()

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('A', 'B')
g.add_edge('A', 'C')

g.add_edge('B', 'A')
g.add_edge('B', 'B')
g.add_edge('B', 'C')

g.add_edge('C', 'D')
g.add_edge('D', 'C')

g.bft('B')

# order: B, then A, C, then D


print(g.vertices)