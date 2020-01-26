from collections import deque
import math
import random
from disjointsets import DisjointSets
from pq import PQ
import timeit

# Programming Assignment 3
# (5) After doing steps 1 through 4 below (look for relevant comments), return up here.
#     Given the output of steps 3 and 4, how does the runtime of Dijkstra's algorithm compare to Bellman-Ford?
#     Does graph density affect performance?  Does size of the graph otherwise affect performance?
#     Is Dijkstra always faster than Bellman-Ford?  If not, when is Bellman-Ford faster?



def generate_random_weighted_digraph(v,e,min_w,max_w) :
    """Generates and returns a random weighted directed graph with v vertices and e different edges.

    Keyword arguments:
    v - number of vertices
    e - number of edges
    min_w - minimum weight
    max_w - maximum weight
    """

    # ensure all vertices reachable from 0
    temp = [ x for x in range(1,v) ]
    random.shuffle(temp)
    temp.append(0)
    temp.reverse()
    edges = [ (temp[random.randrange(0,i)],temp[i]) for i in range(1,v) ]

    # if desired number of edges greater than length of current edge list, then add more edges
    if e > len(edges) :
        edgeSet = { x for x in edges }
        notYetUsedEdges = [ (x,y) for x in range(v) for y in range(v) if x != y and (x,y) not in edgeSet ]
        random.shuffle(notYetUsedEdges)
        count = e - len(edges)
        count = min(count, len(notYetUsedEdges))
        for i in range(count) :
            edges.append(notYetUsedEdges.pop())

    # generate random edge weights
    weights = [ random.randint(min_w, max_w) for x in range(len(edges)) ]

    # construct a Digraph with the lists of edges and weights generated
    G = Digraph(v, edges, weights)
    return G
            



def time_shortest_path_algs() :
    """Generates a table of timing results comparing two versions of Dijkstra's algorithm."""
    
    # Programming Assignment 3
    #
    # (3) Make sure you find steps 1 and 2 later in this module (in this file in the Digraph class) then
    #     return up here to finish assignment.
    #     Implement this function to do the following:
    #     -- Call generate_random_weighted_graph from above to generate a random weighted
    #        directed graph with 16 vertices and 240 edges
    #        (i.e., completely connected--all possible directed edges, other than loops)
    #        and weights random in interval 1 to 10 inclusive.
    #     -- Read documentation of timeit (https://docs.python.org/3/library/timeit.html)
    #     -- Use timeit to time both Bellman-Ford and Dijkstra that you implemented in steps 1 and 2 on this graph.
    #        The number parameter to timeit controls how many times the thing you're timing is called.
    #        To get meaningful times, you will need to experiment with this
    #        a bit.  E.g., increase it if the times are too small.  Use the same value of number for timing both algorithms.
    #        IMPORTANT: Definitely don't use the default value of number, which is something like 1000000.
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
    #     -- If you want, you can include larger digraphs.
    #        The pattern I used when indicating what size to use:
    #        Dense graphs: v, e=v*(v-1).
    #        Sparse: v, e=2*v.
    #        Something in the middle: v, e=v*(v-1)/lg v.
    #        For example, if you want to continue the experimentation with larger graphs, you might
    #        try 1024 vertices with 1047552 edges (dense graph), 1024 vertices with 2048 edges (sparse),
    #        and 1024 vertices with 104755 edges (somewhere between dense and sparse).
    #Create Graphs
    small_graph_32 = generate_random_weighted_digraph(16, 32, 1, 10)
    small_graph_60 = generate_random_weighted_digraph(16, 60, 1, 10)
    small_graph_240 = generate_random_weighted_digraph(16, 240, 1, 10)

    medium_graph_128 = generate_random_weighted_digraph(64, 128, 1, 10)
    medium_graph_672 = generate_random_weighted_digraph(64, 672, 1, 10)
    medium_graph_4032 = generate_random_weighted_digraph(64, 4032, 1, 10)

    large_graph_512 = generate_random_weighted_digraph(256, 512, 1, 10)
    large_graph_8160 = generate_random_weighted_digraph(256, 8160, 1, 10)
    large_graph_65280 = generate_random_weighted_digraph(256, 65280, 1, 10)
    
    # Output
    print("%0s %18s %10s %10s" % ("Algorithm", "Vertices", "Edges", "Time"))
    print('=' * 54)
    print("%0s %10s %13s %16s" % ("Bellman Ford", "16", "32", "%.5f" % timeit.timeit(lambda : small_graph_32.bellman_ford(0), number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra    ", "16", "32", "%.5f" % timeit.timeit(lambda : small_graph_32.dijkstra(0), number=10000)))

    print("%0s %10s %13s %16s" % ("Bellman Ford", "16", "60", "%.5f" % timeit.timeit(lambda : small_graph_60.bellman_ford(0), number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra    ", "16", "60", "%.5f" % timeit.timeit(lambda : small_graph_60.dijkstra(0), number=10000)))

    print("%0s %10s %13s %16s" % ("Bellman Ford", "16", "240", "%.5f" % timeit.timeit(lambda : small_graph_240.bellman_ford(0), number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra    ", "16", "240", "%.5f" % timeit.timeit(lambda : small_graph_240.dijkstra(0), number=10000)))

    print("%0s %10s %13s %16s" % ("Bellman Ford", "64", "128", "%.5f" % timeit.timeit(lambda : medium_graph_128.bellman_ford(0), number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra    ", "64", "128", "%.5f" % timeit.timeit(lambda : medium_graph_128.dijkstra(0), number=10000)))

    print("%0s %10s %13s %16s" % ("Bellman Ford", "64", "672", "%.5f" % timeit.timeit(lambda : medium_graph_672.bellman_ford(0), number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra    ", "64", "672", "%.5f" % timeit.timeit(lambda : medium_graph_672.dijkstra(0), number=10000)))

    print("%0s %10s %13s %16s" % ("Bellman Ford", "64", "4032", "%.5f" % timeit.timeit(lambda : medium_graph_4032.bellman_ford(0), number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra    ", "64", "4032", "%.5f" % timeit.timeit(lambda : medium_graph_4032.dijkstra(0), number=10000)))

    print("%0s %10s %13s %16s" % ("Bellman Ford", "256", "512", "%.5f" % timeit.timeit(lambda : large_graph_512.bellman_ford(0), number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra    ", "256", "512", "%.5f" % timeit.timeit(lambda : large_graph_512.dijkstra(0), number=10000)))

    print("%0s %10s %13s %16s" % ("Bellman Ford", "256", "8160", "%.5f" % timeit.timeit(lambda : large_graph_8160.bellman_ford(0), number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra    ", "256", "8160", "%.5f" % timeit.timeit(lambda : large_graph_8160.dijkstra(0), number=10000)))

    print("%0s %10s %13s %16s" % ("Bellman Ford", "256", "65280", "%.5f" % timeit.timeit(lambda : large_graph_65280.bellman_ford(0), number=10000)))
    print("%0s %10s %13s %16s" % ("Dijkstra    ", "256", "65280", "%.5f" % timeit.timeit(lambda : large_graph_65280.dijkstra(0), number=10000)))
    return("Finished")


    




class Graph :
    """Graph represented with adjacency lists."""

    __slots__ = ['_adj']

    def __init__(self, v=10, edges=[], weights=[]) :
        """Initializes a graph with a specified number of vertices.

        Keyword arguments:
        v - number of vertices
        edges - any iterable of ordered pairs indicating the edges 
        weights - (optional) list of weights, same length as edges list
        """

        self._adj = [ _AdjacencyList() for i in range(v) ]
        i=0
        hasWeights = len(edges)==len(weights)
        for a, b in edges :
            if hasWeights :
                self.add_edge(a,b,weights[i])
                i = i + 1
            else :
                self.add_edge(a, b)



    def add_edge(self, a, b, w=None) :
        """Adds an edge to the graph.

        Keyword arguments:
        a - first end point
        b - second end point
        w - weight for the edge (optional)
        """

        self._adj[a].add(b, w)
        self._adj[b].add(a, w)
    

    def num_vertices(self) :
        """Gets number of vertices of graph."""
        
        return len(self._adj)


    def degree(self, vertex) :
        """Gets degree of specified vertex.

        Keyword arguments:
        vertex - integer id of vertex
        """
        
        return self._adj[vertex]._size

    def bfs(self, s) :
        """Performs a BFS of the graph from a specified starting vertex.
        Returns a list of objects, one per vertex, containing the vertex's distance
        from s in attribute d, and vertex id of its predecessor in attribute pred.

        Keyword arguments:
        s - the integer id of the starting vertex.
        """
        
        class VertexData :
            __slots__ = [ 'd', 'pred' ]

            def __init__(self) :
                self.d = math.inf
                self.pred = None

        vertices = [VertexData() for i in range(len(self._adj))]
        vertices[s].d = 0
        q = deque([s])
        while len(q) > 0 :
            u = q.popleft()
            for v in self._adj[u] :
                if vertices[v].d == math.inf :
                    vertices[v].d = vertices[u].d + 1
                    vertices[v].pred = u
                    q.append(v)
        return vertices

    def dfs(self) :
        """Performs a DFS of the graph.  Returns a list of objects, one per vertex, containing
        the vertex's discovery time (d), finish time (f), and predecessor in the depth first forest
        produced by the search (pred).
        """

        class VertexData :
            __slots__ = [ 'd', 'f', 'pred' ]

            def __init__(self) :
                self.d = 0
                self.pred = None

        vertices = [VertexData() for i in range(len(self._adj))]
        time = 0

        def dfs_visit(u) :
            nonlocal time
            nonlocal vertices

            time = time + 1
            vertices[u].d = time
            for v in self._adj[u] :
                if vertices[v].d == 0 :
                    vertices[v].pred = u
                    dfs_visit(v)
            time = time + 1
            vertices[u].f = time

        for u in range(len(vertices)) :
            if vertices[u].d == 0 :
                dfs_visit(u)
        return vertices


    def print_graph(self, with_weights=False) :
        """Prints the graph."""
        
        for v, vList in enumerate(self._adj) :
            print(v, end=" -> ")
            if with_weights :
                for u, w in vList.__iter__(True) :
                    print(u, "(" + str(w) + ")", end="\t")
            else :
                for u in vList :
                    print(u, end="\t")
            print()

    def get_edge_list(self, with_weights=False) :
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
        for v, vList in enumerate(self._adj) :
            if with_weights :
                for u, w in vList.__iter__(True) :
                    edges.append(((v,u),w))
            else :
                for u in vList :
                    edges.append((v,u))
        return edges

    def mst_kruskal(self) :
        """Returns the set of edges in some
        minimum spanning tree (MST) of the graph,
        computed using Kruskal's algorithm.
        """
        
        A = set()
        forest = DisjointSets(len(self._adj))
        edges = self.get_edge_list(True)
        edges.sort(key=lambda x : x[1])
        for e, w in edges :
            if forest.find_set(e[0]) != forest.find_set(e[1]) :
                A.add(e)
                #A = A | {e}
                forest.union(e[0],e[1])
        return A


    def mst_prim(self, r=0) :
        """Returns the set of edges in some
        minimum spanning tree (MST) of the graph,
        computed using Prim's algorithm.

        Keyword arguments:
        r - vertex id to designate as the root (default is 0).
        """

        parent = [ None for x in range(len(self._adj))]
        Q = PQ()
        Q.add(r, 0)
        for u in range(len(self._adj)) :
            if u != r :
                Q.add(u, math.inf)
        while not Q.is_empty() :
            u = Q.extract_min()
            for v, w in self._adj[u].__iter__(True) :
                if Q.contains(v) and w < Q.get_priority(v) :
                    parent[v] = u
                    Q.change_priority(v, w)
        A = set()
        for v, u in enumerate(parent) :
            if u != None :
                A.add((u,v))
                #A = A | {(u,v)}
        return A




class Digraph(Graph) :

    def __init__(self, v=10, edges=[], weights=[]) :
        super(Digraph, self).__init__(v, edges, weights)

    def add_edge(self, a, b, w=None) :
        self._adj[a].add(b, w)

    
    def bellman_ford(self,s) :
        """Bellman Ford Algorithm for single source shortest path.

        Keyword Arguments:
        s - The source vertex.
        Page 651
        """

        # Programming Assignment 3:
        # 1) Implement Bellman Ford Algorithm.
        #
        #    If there are negative weight cycles, have this method return an empty list (instead of the False from the
        #    pseudocode).
        #
        #    If there are no negative weight cycles, then
        #    have this method return a list of 3-tuples, one for each vertex, such that first position is vertex id,
        #    second is distance from source vertex (i.e., what pseudocode from textbook refers to as v.d), and third
        #    is the vertex's parent (what the textbook refers to as v.pi).  E.g., (2, 10, 5) would mean the shortest path
        #    from s to 2 has weight 10, and vertex 2's parent is vertex 5.
        #
        #    the parameter s is the source vertex.
        #
        # Useful Hint (for both parts 1 and 2):
        #  The loops of lines 3 and 5 of the pseudocode for Bellman Ford iterate over the edges
        #  of the graph.  You will also need the weights.  The adjacency list class has two iterators,
        #  one that gives you the weights and one that doesn't.  To implement the iteration over the
        #  edges, you will actually need a pair of nested loops, one over the vertices u, and then one
        #  over the edges that start at u (along with the weights of those edges).
        #  To iterate over the vertices adjacent to u, and the get the weight associated with each edge, you can do:
        #  for v, w in self._adj[u].__iter__(True)
        #  You don't normally call methods that start with __ directly.  Python's for loops call
        #  that method to control how many times to iterate when iterating over a collection like a list.
        #  I provided an optional parameter to that method, which when passed True, gives you the
        #  adjacent vertices and the edge weights.
        #
        #  When you get to part 2 later, when you implement Dijkstra's algorithm, you will need to do a similar
        #  thing (line 7 of the pseduocode of Dijkstra's algorithm).  Only there you'll just iterate over the
        #  vertices adjacent to u, and not all of the edges.

        distance = [math.inf] * len(self._adj)
        distance[s] = 0
        parent = [None for x in self._adj]
        
        for v, vList in enumerate(self._adj):
            for u, w in vList.__iter__(True) :
                if distance[u] != math.inf and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    parent[v] = u

        #Check for Negative Weights
        for v, vList in enumerate(self._adj):
            for u, w in vList.__iter__(True):
                if distance[u] != math.inf and distance[u] + w < distance[v]:
                    return []
        return distance






    def dijkstra(self,s) :
        """Dijkstra's Algorithm using a binary heap as the PQ.

        Keyword Arguments:
        s - The source vertex.
        Page 658
        """

        # Programming Assignment 3:
        # 2) Implement Dijkstra's Algorithm using a binary heap implementation of a PQ as the PQ.
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


class _AdjacencyList :

    __slots__ = [ '_first', '_last', '_size']

    def __init__(self) :
        self._first = self._last = None
        self._size = 0

    def add(self, node, w=None) :
        if self._first == None :
            self._first = self._last = _AdjListNode(node, w)
        else :
            self._last._next = _AdjListNode(node, w)
            self._last = self._last._next
        self._size = self._size + 1

    def __iter__(self, weighted=False):
        if weighted :
            return _AdjListIterWithWeights(self)
        else :
            return _AdjListIter(self)

    

    

class _AdjListNode :

    __slots__ = [ '_next', '_data', '_w' ]

    def __init__(self, data, w=None) :
        self._next = None
        self._data = data
        self._w = w

        

class _AdjListIter :

    __slots__ = [ '_next', '_num_calls' ]

    def __init__(self, adj_list) :
        self._next = adj_list._first
        self._num_calls = adj_list._size

    def __iter__(self) :
        return self

    def __next__(self) :
        if self._num_calls == 0 :
            raise StopIteration
        self._num_calls = self._num_calls - 1
        data = self._next._data
        self._next = self._next._next
        return data

class _AdjListIterWithWeights :

    __slots__ = [ '_next', '_num_calls' ]

    def __init__(self, adj_list) :
        self._next = adj_list._first
        self._num_calls = adj_list._size

    def __iter__(self) :
        return self

    def __next__(self) :
        if self._num_calls == 0 :
            raise StopIteration
        self._num_calls = self._num_calls - 1
        data = self._next._data
        w = self._next._w
        self._next = self._next._next
        return data, w




if __name__ == "__main__" :
        
    # here is where you will implement any code necessary to confirm that your
    # methods work correctly.
    # Code in this if block will only run if you run this module, and not if you load this module with
    # an import for use by another module.

    # (4) Call your time_shortest_path_algs() function here to output the results of step 3.

    graphtest = generate_random_weighted_digraph(16, 60, 1, 10)
    print(graphtest.dijkstra(0))
    #Graph.print_graph(graphtest)
    print(graphtest.bellman_ford(0))
    #Graph.print_graph(graphtest)
    #time_shortest_path_algs()
    
