# Gregory Walsh
# DSA II SPRING 2018
# Programming Assignment 3
from collections import deque
import math
from disjointsets import DisjointSets
from pq import PQ
from random import *
import timeit


# Programming Assignment 3
# (5) After doing steps 1 through 4 below (look for relevant comments), return up here.
#     Given the output of step 4, how do the 2 versions of Dijkstra's algorithm compare?
#     How does graph density affect performance?  Does size of the graph otherwise affect performance?
#     Any other observations?
#
#     The 2 versions of Dijkstras algorithm were very interesting to compare. Version 1 used a list as the priority queue and Version 2 used a Binary Heap for the priority queue. From what we learned in class the runtime of version 1 is O(V^2) adn the runtime of Version 2 is  O(E lg V). The Programming assignment demonstrated this faster time in versions very well. From the results it was clear to see Version 2 was much quicker than Version 1. When the graphs began to get more dense it took longer to compute the runtimes of each algorithm. When testing graphs with 64 and 256 vertices it got very difficult to compute the final times of the algorithm. In order to get results I needed to lower the amount of iterations the 'number' field in timeit. This does make results alittle inaccurate however it still allows the overall picture to be viewed that Version 1 of Dijkstra is slower than Version 2. The amount of verticies affected the graph because the size of the graph grew and the for loop needs to iterate over more vertices in order to perform INSERT. From the results, the amount of edges of the graph impacted the time immensely. As the edge count went higher the time to run through the algorithms increased as well. Version 1 got impacted more than Version 2 however to see Version 2's time of completion get to over 4-5 seconds is pretty huge. I think this is because the EXTRACT-MIN and DECREASE-KEY needing to do more checks for the edge weights. When looking at vertices of 64 and edges 128,672,4032 the time for both algorithms increased from V1:(6,39,96) and V2:(2,5,19) NOTE: These numbers are from one trial and are averaged. These numbers show as the edges increased so did the time needed for BOTH algorithms to solve the Graphs. On a side note, timeit gave me problems trying to pass a loop of each graph through and running timeit so I needed to create a seperate def for each graph which is ugly and a brute force approach. It allows me to get the required info however. This was a very challenging programming assignment for me and I learned a lot.


def generate_random_weighted_digraph(v, e, min_w, max_w):
    """Generates and returns a random weighted directed graph with v vertices and e different edges.

    Keyword arguments:
    v - number of vertices
    e - number of edges
    min_w - minimum weight
    max_w - maximum weight
    """

    # Programming Assignment 3
    # ✔(1) Implement this function, which should:
    #    -- ✔Generate a random weighted directed graph with v vertices and e different edges.
    #    -- ✔Start by generating a list of random edges (assume vertices numbered from 0 to v-1).
    #       In this list, each edge is a 2-tuple, e.g., (2, 3) is an edge from vertex 2 to vertex 3.
    #    -- ✔Next, generate a list, the same length, of random weights, with minW and maxW specifying the
    #       range of weights.
    #    -- ✔Then construct a Digraph object passing your lists above as parameters.  The Digraph class extends
    #       Graph so actually has the same __init__ parameters as its parent class.
    #    -- ✔return that Digraph object
    change = []
    randomedgelist = [(randint(0, v - 1), randint(0, v - 1)) for i in range(e)]
    randomweightlist = [(randint(min_w, max_w)) for i in range(e)]
    for i in randomedgelist:
        if i[0] == i[1]:
            change = randomedgelist.index(i)
            randomweightlist[change] = 0
    return Digraph(v, randomedgelist, randomweightlist)


def time_shortest_path_algs():
    """Generates a table of timing results comparing two versions of Dijkstra's algorithm."""

    # Programming Assignment 3
    #
    # (4) Make sure you find steps 2 and 3 later in this module (laster in this file in the Digraph class) then
    #     return up here to finish assignment.
    #     Implement the following function to do the following:
    #     -- Use your function from step (1) generate a random weighted directed graph with 16 vertices and 240 edges
    #        (i.e., completely connected--all possible directed edges) and weights random in interval 1 to 10 inclusive.
    #     -- Read documentation of timeit (https://docs.python.org/3/library/timeit.html)
    #     -- Use timeit to time both versions of Dijkstra that you implemented in steps 2 and 3 on this graph.  The number parameter
    #        to timeit controls how many times the thing you're timing is called.  To get meaningful times, you will need to experiment with this
    #        a bit.  E.g., increase it if the times are too small.  Use the same value of number for timing both algorithms.
    #     -- Now repeat this for a digraph with 64 vertices and 4032 edges.
    #     -- Now repeat this for a digraph with 256 vertices and 65280 edges.
    #     -- Now repeat for 16 vertices and 60 edges.
    #     -- Now repeat for 64 vertices and 672 edges.
    #     -- Now repeat for 256 vertices and 8160 edges.
    #     -- Repeat this again for 16 vertices and 32 edges.
    #     -- Repeat yet again with 64 vertices and 128 edges.
    #     -- Repeat yet again with 256 vertices and 512 edges.
    #
    #     -- Have this function output the timing data in a table, with columns for number of vertices, number of edges, and time.
    #     -- If you want, you can include larger digraphs.  The pattern I used when indicating what size to use: Dense graphs: v, e=v*(v-1),
    #        Sparse: v, e=2*v, and Something in the middle: v, e=v*(v-1)/lg V.

    # Generate the Digraphs
    graph1632 = generate_random_weighted_digraph(16, 32, 1, 10)
    graph16240 = generate_random_weighted_digraph(16, 240, 1, 10)
    graph1660 = generate_random_weighted_digraph(16, 60, 1, 10)

    graph64128 = generate_random_weighted_digraph(64, 128, 1, 10)
    graph64672 = generate_random_weighted_digraph(64, 672, 1, 10)
    graph644032 = generate_random_weighted_digraph(64, 4032, 1, 10)

    graph256512 = generate_random_weighted_digraph(256, 512, 1, 10)
    graph2568160 = generate_random_weighted_digraph(256, 8160, 1, 10)
    graph25665280 = generate_random_weighted_digraph(256, 65280, 1, 10)

    # Since Timeit would only work with functions I had to make seperate ones for each Graph. Ugly, I know but it works.
    # graph1632
    def graph1632V1():
        graph1632.dijkstras_version_1(0)

    def graph1632V2():
        graph1632.dijkstras_version_2(0)

    # graph16240
    def graph16240V1():
        graph16240.dijkstras_version_1(0)

    def graph16240V2():
        graph16240.dijkstras_version_2(0)

    # graph1660
    def graph1660V1():
        graph1660.dijkstras_version_1(0)

    def graph1660V2():
        graph1660.dijkstras_version_2(0)

    # graph64128
    def graph64128V1():
        graph64128.dijkstras_version_1(0)

    def graph64128V2():
        graph64128.dijkstras_version_2(0)

    # graph644032
    def graph644032V1():
        graph644032.dijkstras_version_1(0)

    def graph644032V2():
        graph644032.dijkstras_version_2(0)

    # graph 64672
    def graph64672V1():
        graph64672.dijkstras_version_1(0)

    def graph64672V2():
        graph64672.dijkstras_version_2(0)

    # graph256512
    def graph256512V1():
        graph256512.dijkstras_version_1(0)

    def graph256512V2():
        graph256512.dijkstras_version_2(0)

    # graph2568160
    def graph2568160V1():
        graph2568160.dijkstras_version_1(0)

    def graph2568160V2():
        graph2568160.dijkstras_version_2(0)

    # graph25665280
    def graph25665280V1():
        graph25665280.dijkstras_version_1(0)

    def graph25665280V2():
        graph25665280.dijkstras_version_2(0)

    # Begin Printout Formatting
    print("%0s %20s %10s %10s" % ("Version", "Vertices", "Edges", "Time"))
    print('-' * 53)

    print("%0s %10s %13s %16s" % ("Dijkstra v1", "16", "32", "%.5f" % timeit.timeit(graph1632V1, number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra v2", "16", "32", "%.5f" % timeit.timeit(graph1632V2, number=10000)))

    print("%0s %10s %13s %16s" % ("Dijkstra v1", "16", "60", "%.5f" % timeit.timeit(graph1660V1, number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra v2", "16", "60", "%.5f" % timeit.timeit(graph1660V2, number=10000)))

    print("%0s %10s %13s %16s" % ("Dijkstra v1", "16", "240", "%.5f" % timeit.timeit(graph16240V1, number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra v2", "16", "240", "%.5f" % timeit.timeit(graph16240V2, number=10000)))

    print("%0s %10s %13s %16s" % ("Dijkstra v1", "64", "128", "%.5f" % timeit.timeit(graph64128V1, number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra v2", "64", "128", "%.5f" % timeit.timeit(graph64128V2, number=10000)))

    print("%0s %10s %13s %16s" % ("Dijkstra v1", "64", "672", "%.5f" % timeit.timeit(graph64672V1, number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra v2", "64", "672", "%.5f" % timeit.timeit(graph64672V2, number=10000)))

    print("%0s %10s %13s %16s" % ("Dijkstra v1", "64", "4032", "%.5f" % timeit.timeit(graph644032V1, number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra v2", "64", "4032", "%.5f" % timeit.timeit(graph644032V2, number=10000)))

    print("%0s %10s %13s %16s" % ("Dijkstra v1", "256", "512", "%.5f" % timeit.timeit(graph256512V1, number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra v2", "256", "512", "%.5f" % timeit.timeit(graph256512V2, number=10000)))

    print("%0s %10s %13s %16s" % ("Dijkstra v1", "256", "8160", "%.5f" % timeit.timeit(graph2568160V1, number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra v2", "256", "8160", "%.5f" % timeit.timeit(graph2568160V2, number=10000)))

    print("%0s %10s %13s %16s" % ("Dijkstra v1", "256", "65280", "%.5f" % timeit.timeit(graph25665280V1, number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra v2", "256", "65280", "%.5f" % timeit.timeit(graph25665280V2, number=10000)))


class Graph:
    """Graph represented with adjacency lists."""

    __slots__ = ['_adj']

    def __init__(self, v=10, edges=[], weights=[]):
        """Initializes a graph with a specified number of vertices.

        Keyword arguments:
        v - number of vertices
        edges - any iterable of ordered pairs indicating the edges
        weights - (optional) list of weights, same length as edges list
        """

        self._adj = [_AdjacencyList() for i in range(v)]
        i = 0
        hasWeights = len(edges) == len(weights)
        for a, b in edges:
            if hasWeights:
                self.add_edge(a, b, weights[i])
                i = i + 1
            else:
                self.add_edge(a, b)

    def add_edge(self, a, b, w=None):
        """Adds an edge to the graph.

        Keyword arguments:
        a - first end point
        b - second end point
        w - weight for the edge (optional)
        """

        self._adj[a].add(b, w)
        self._adj[b].add(a, w)

    def num_vertices(self):
        """Gets number of vertices of graph."""

        return len(self._adj)

    def degree(self, vertex):
        """Gets degree of specified vertex.

        Keyword arguments:
        vertex - integer id of vertex
        """

        return self._adj[vertex]._size

    def bfs(self, s):
        """Performs a BFS of the graph from a specified starting vertex.
        Returns a list of objects, one per vertex, containing the vertex's distance
        from s in attribute d, and vertex id of its predecessor in attribute pred.

        Keyword arguments:
        s - the integer id of the starting vertex.
        """

        class VertexData:
            __slots__ = ['d', 'pred']

            def __init__(self):
                self.d = math.inf
                self.pred = None

        vertices = [VertexData() for i in range(len(self._adj))]
        vertices[s].d = 0
        q = deque([s])
        while len(q) > 0:
            u = q.popleft()
            for v in self._adj[u]:
                if vertices[v].d == math.inf:
                    vertices[v].d = vertices[u].d + 1
                    vertices[v].pred = u
                    q.append(v)
        return vertices

    def dfs(self):
        """Performs a DFS of the graph.  Returns a list of objects, one per vertex, containing
        the vertex's discovery time (d), finish time (f), and predecessor in the depth first forest
        produced by the search (pred).
        """

        class VertexData:
            __slots__ = ['d', 'f', 'pred']

            def __init__(self):
                self.d = 0
                self.pred = None

        vertices = [VertexData() for i in range(len(self._adj))]
        time = 0

        def dfs_visit(u):
            nonlocal time
            nonlocal vertices

            time = time + 1
            vertices[u].d = time
            for v in self._adj[u]:
                if vertices[v].d == 0:
                    vertices[v].pred = u
                    dfs_visit(v)
            time = time + 1
            vertices[u].f = time

        for u in range(len(vertices)):
            if vertices[u].d == 0:
                dfs_visit(u)
        return vertices

    def print_graph(self, with_weights=False):
        """Prints the graph."""

        for v, vList in enumerate(self._adj):
            print(v, end=" -> ")
            if with_weights:
                for u, w in vList.__iter__(True):
                    print(u, "(" + str(w) + ")", end="\t")
            else:
                for u in vList:
                    print(u, end="\t")
            print()

    def get_edge_list(self, with_weights=False):
        """Returns a list of the edges of the graph
        as a list of tuples.  Default is of the form
        [ (a, b), (c, d), ... ] where a, b, c, d, etc are
        vertex ids.  If with_weights is True, the generated
        list includes the weights in the following form
        [ ((a, b), w1), ((c, d), w2), ... ] where w1, w2, etc
        are the edge weights.

        Keyword arguments:
        with_weights -- True to include weights
        """

        edges = []
        for v, vList in enumerate(self._adj):
            if with_weights:
                for u, w in vList.__iter__(True):
                    edges.append(((v, u), w))
            else:
                for u in vList:
                    edges.append((v, u))
        return edges

    def mst_kruskal(self):
        """Returns the set of edges in some
        minimum spanning tree (MST) of the graph,
        computed using Kruskal's algorithm.
        """

        A = set()
        forest = DisjointSets(len(self._adj))
        edges = self.get_edge_list(True)
        edges.sort(key=lambda x: x[1])
        for e, w in edges:
            if forest.find_set(e[0]) != forest.find_set(e[1]):
                A.add(e)
                # A = A | {e}
                forest.union(e[0], e[1])
        return A

    def mst_prim(self, r=0):
        """Returns the set of edges in some
        minimum spanning tree (MST) of the graph,
        computed using Prim's algorithm.

        Keyword arguments:
        r - vertex id to designate as the root (default is 0).
        """

        parent = [None for x in range(len(self._adj))]
        Q = PQ()
        Q.add(r, 0)
        for u in range(len(self._adj)):
            if u != r:
                Q.add(u, math.inf)
        while not Q.is_empty():
            u = Q.extract_min()
            for v, w in self._adj[u].__iter__(True):
                if Q.contains(v) and w < Q.get_priority(v):
                    parent[v] = u
                    Q.change_priority(v, w)
        A = set()
        for v, u in enumerate(parent):
            if u != None:
                A.add((u, v))
                # A = A | {(u,v)}
        return A


class Digraph(Graph):

    def __init__(self, v=10, edges=[], weights=[]):
        super(Digraph, self).__init__(v, edges, weights)

    def add_edge(self, a, b, w=None):
        self._adj[a].add(b, w)

    def dijkstras_version_1(self, s):
        """Dijkstra's Algorithm using a simple list as the PQ."""

        # Programming Assignment 3:
        # 2) Implement Dijkstra's Algorithm using a simple list as the "priority queue" as described in paragraph
        #    that starts at bottom of page 661 and continues on 662 (also described in class).
        #
        #    Have this method return a list of 3-tuples, one for each vertex, such that first position is vertex id,
        #    second is distance from source vertex (i.e., what pseudocode from textbook refers to as v.d), and third
        #    is the vertex's parent (what the textbook refers to as v.pi).  E.g., (2, 10, 5) would mean the shortest path
        #    from s to 2 has weight 10, and vertex 2's parent is vertex 5.
        #
        #    the parameter s is the source vertex.

        # Need this for some reason???
        class VertexData:
            pass

        def Relax(self, u, v):
            for a, w in self._adj[u].__iter__(True):
                if a == v:
                    if vertices[v].d > vertices[u].d + w:
                        vertices[v].d = vertices[u].d + w
                        vertices[v].pred = u
                        List[v] = vertices[v].d

        vertices = [VertexData() for i in range(len(self._adj))]
        List = []
        S = []
        for i in range(len(vertices)):
            vertices[i].d = math.inf
            vertices[i].pred = None
            List.append(vertices[i].d)
        vertices[s].d = 0
        List[s] = vertices[s].d
        while len(S) != len(List):
            inf = math.inf
            u = 0
            for i in range(len(List)):
                if List[i] != None:
                    if List[i] < inf:
                        inf = List[i]
                        u = i
            S.append((u, inf, vertices[u].pred))
            List[u] = None
            for v in self._adj[u]:
                Relax(self, u, v)
        return S

    def dijkstras_version_2(self, s):
        """Dijkstra's Algorithm using a binary heap as the PQ."""

        # Programming Assignment 3:
        # 3) Implement Dijkstra's Algorithm using a binary heap implementation of a PQ as the PQ.
        #    Specifically, use the implementation I have posted here: https://github.com/cicirello/PythonDataStructuresLibrary
        #    Use the download link (if you simply click pq.py Github will just show you the source in a web browser with line numbers).
        #
        #    Have this method return a list of 3-tuples, one for each vertex, such that first position is vertex id,
        #    second is distance from source vertex (i.e., what pseudocode from textbook refers to as v.d), and third
        #    is the vertex's parent (what the textbook refers to as v.pi).  E.g., (2, 10, 5) would mean the shortest path
        #    from s to 2 has weight 10, and vertex 2's parent is vertex 5.
        #
        #    the parameter s is the source vertex.
        distance = [math.inf for x in self._adj]
        parent = [None for x in self._adj]
        Q = PQ()
        distance[s] = 0
        Q.add(s, 0)
        S = []
        for u in range(len(self._adj)):
            if u != s:
                Q.add(u, math.inf)
        while not Q.is_empty():
            u = Q.extract_min()
            S.append(u)
            for v, w in self._adj[u].__iter__(True):
                if (distance[u] + w) < distance[v]:
                    parent[v] = u
                    distance[v] = (distance[u] + w)
        returnlist = []
        for v in S:
            returnlist.append((v, distance[v], parent[v]))
        return returnlist

    def dijkstras_version_3(self, s):
        # Programming Assignment 3:
        # EXTRA CREDIT 6: Make sure you do all required parts, assignment steps 1 to 5, before
        # even considering doing this optional extra credit part.
        #
        # Implement Dijkstra's Algorithm using a fibonacci heap implementation of a PQ as the PQ.
        # To do this, you must first implement a fibonacci heap (see the textbook chapter on fibonacci
        # heaps, Chapter 19).  You are not allowed to use an existing fibonacci heap class found from
        # the internet.  If you do the extra credit, you must implement your own.  Put your fibonacci heap class
        # in a separate .py file and make sure you include it with your homework submission.
        # Your dijkstras algorithm implementation here that uses it should have the same return
        # type as the previous two versions from steps 2 and 3 of the assignment.
        # If you do the extra credit portion, then modify your step 4 to include this version in the
        # timing results.
        #
        # This is worth very substantial extra credit if you do it, and if you do it correctly.  Implementing
        # the fibonacci heap is at least as hard (probably harder) than the first 3 programming assignments
        # combined.
        pass

    def topological_sort(self):
        """Topological Sort of the directed graph (Section 22.4 from textbook).
        Returns the topological sort as a list of vertex indices.
        """

        pass  # Remove this pass statement after you implement this method.  Simply here temporarily.

        #       Homework Hints/Suggestions/Etc:
        #           1) Textbook indicates to use a Linked List.  Python doesn't have
        #               one in the standard library.  Instead, use a deque (don't simply use
        #               a python list since adding at the front is O(N) for a python list,
        #               while it is O(1) for a deque).
        #           2) From the pseudocode, you will be tempted to (a) call DFS, and then (b) sort
        #               vertices by the finishing times.  However, don't do that since the sort will
        #               cost O(V lg V) unnecessarily.
        #           3) So, how do you do it without sorting?
        #               A) Option A: Start by copying and pasting DFS code to start of topologicalSort, and
        #                   where finishing time is set, add the vertex index to front of list.
        #               B) Option B: Add an optional parameter to DFS method that is a
        #                   function that is called upon finishing a vertex.
        #                   Give it a default that does nothing (i.e., just a pass). Your topologicalSort would then
        #                   call DFS passing a function that adds the vertex index to the front of a list.
        #               C) Option C: any other way you can come up with that doesn't change what DFS currently does logically

    def transpose(self):
        """Computes the transpose of a directed graph. (See textbook page 616 for description of transpose).
        Does not alter the self object.  Returns a new Digraph that is the transpose of self."""

        pass  # Remove this pass statement after you implement this method.  Simply here temporarily.

    def strongly_connected_components(self):
        """Computes the strongly connected components of a digraph.
        Returns a list of lists, containing one list for each strongly connected component,
        which is simply a list of the vertices in that component."""

        pass  # Remove this pass statement after you implement this method.  Simply here temporarily.

        #       Homework Hints/Suggestions/Etc: See algorithm on page 617.
        #           1) Take a look at steps 1 and 2 before you do anything.  Notice that Step 1 computes finishing times with DFS,
        #               and step 3 uses vertices in order of decreasing finishing times.  As in the topological sort, don't actually sort
        #               by finishing time (to avoid O(V lg v) step).  However, this is easier than in the topological sort as you already
        #               have a method that will get you what you need.  For step 1 of algorithm you can simply call your topological sort.
        #               That will give you the vertices in decreasing order by finishing time, which is really the intention of line 1.
        #           2) Line 2 is just the transpose and you implemented a method to compute this above.
        #           3) The DFS in line 3 can be done in a couple ways.  As above, if you change DFS, make sure it will still function in the basic
        #               version.  The simplest way to do that would be to leave it alone, and just start by copying and pasting the code.
        #               You'll need to then alter it to have the outer loop use the vertex ordering obtained from algorithm line 1 (to implement line 3).
        #               And to do line 4, you'll need to further alter it to generate the list of lists for the return value.


class _AdjacencyList:

    __slots__ = ['_first', '_last', '_size']

    def __init__(self):
        self._first = self._last = None
        self._size = 0

    def add(self, node, w=None):
        if self._first == None:
            self._first = self._last = _AdjListNode(node, w)
        else:
            self._last._next = _AdjListNode(node, w)
            self._last = self._last._next
        self._size = self._size + 1

    def __iter__(self, weighted=False):
        if weighted:
            return _AdjListIterWithWeights(self)
        else:
            return _AdjListIter(self)


class _AdjListNode:

    __slots__ = ['_next', '_data', '_w']

    def __init__(self, data, w=None):
        self._next = None
        self._data = data
        self._w = w


class _AdjListIter:

    __slots__ = ['_next', '_num_calls']

    def __init__(self, adj_list):
        self._next = adj_list._first
        self._num_calls = adj_list._size

    def __iter__(self):
        return self

    def __next__(self):
        if self._num_calls == 0:
            raise StopIteration
        self._num_calls = self._num_calls - 1
        data = self._next._data
        self._next = self._next._next
        return data


class _AdjListIterWithWeights:

    __slots__ = ['_next', '_num_calls']

    def __init__(self, adj_list):
        self._next = adj_list._first
        self._num_calls = adj_list._size

    def __iter__(self):
        return self

    def __next__(self):
        if self._num_calls == 0:
            raise StopIteration
        self._num_calls = self._num_calls - 1
        data = self._next._data
        w = self._next._w
        self._next = self._next._next
        return data, w


if __name__ == "__main__":

    # here is where you will implement any code necessary to confirm that your
    # methods work correctly.
    # Code in this if block will only run if you run this module, and not if you load this module with
    # an import for use by another module.
    time_shortest_path_algs()
