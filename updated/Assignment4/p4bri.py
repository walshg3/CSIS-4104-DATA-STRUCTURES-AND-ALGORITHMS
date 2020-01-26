#!/usr/bin/python
# Add any relevant import statements up here.
import math
import sys
# Programming Assignment 4:
# Follow the instuctions in comments throughout this file.
# Don't rename any methods, attributes, functions, etc.
# Also don't change order or type of parameters.  
# You might consider doing the assignment in this order: 1, 2, 5, 6a, 3, 4, 6b.

class WeightedAdjacencyMatrix :

    # Although technically you do not need to declare variables, including object attributes
    # prior to first use, a consequence of that is that Python must allocate more memory than
    # actually needed because it has no way of knowing how much you will need.
    # __slots__ offers a way of being more memory efficient.  It tells Python exactly what
    # attributes this class will have.  In this case, only a field named _W.  So Python will
    # only allocate enough memory for the attributes specified in __slots__ (just separate by commas
    # if you need more than one).
    # If you try to specify an attribute that is not included in this list you will get a runtime
    # exception.
    __slots__ = ['_W']

    # 1) Implement the initializer, which should create a matrix (i.e., list of lists) with
    # number of rows and columns both equal to size (i.e., number of vertices).
    # Initially there are no edges, which means that the weights should all initially
    # be infinity (inf in Python), other than the diagonal which should have 0s (cost of
    # shortest path from a vertex u to itself is 0).
    #
    # Use the attribute I provided above in __slots__ for your matrix _W (see comment above).
    # Remember to use self for an object attribute (i.e., self._W )
    def __init__(self, size) :
        """Initializes a weighted adjacency matrix for a graph with size nodes.

        Graph is initialized with size nodes and 0 edges.
        
        Keyword arguments:
        size -- Number of nodes of the graph.
        """
        
        self._W = list()
        for i in range(size):
            self._W.append(list())
            for j in range(size):
                self._W[i].append(0 if i == j else math.inf)
    

    # 2) Implement this method (see the provided docstring)
    def add_edge(self, u, v, weight) :
        """Adds a directed edge from u to v with the specified weight.

        Keyword arguments:
        u -- source vertex id (0-based index)
        v -- target vertex id (0-based index)
        weight -- edge weight
        """

        self._W[u][v] = weight
    

    # 5) Implement this method (see the provided docstring)
    def floyd_warshall(self) :
        """Floyd Warshall algorithm for all pairs shortest paths.

        Returns a matrix D consisting of the weights of the shortest paths between
        all pairs of vertices.  This method does not change the weight matrix of the graph itself.

        Extra Credit version: Returns a tuple (D, P) where D is a matrix consisting of the
        weights of the shortest paths between all pairs of vertices, and P is the predecessors matrix.
        """

        D = self._W
        P = [[i if e!=math.inf else math.inf for i,e in enumerate(v)] for v in D]
        for k in range(len(self._W)):
            D_next = list()
            P_next = list()
            for i in range(len(self._W)):
                D_next.append(list())
                P_next.append(list())
                for j in range(len(self._W)):
                    if(D[i][k]+D[k][j] < D[i][j]):
                        D_next[i].append(D[i][k]+D[k][j])
                        P_next[i].append(k)
                    else:
                        D_next[i].append(D[i][j])
                        P_next[i].append(P[i][j])
            P = P_next
            D = D_next
        return (D,P)


# 3) Implement this function.  First note the lack of indentation.  This is not a method of the above class.
# It is a function.
# You can find the relevant equation for haversine distance at this link (and others):
# https://www.movable-type.co.uk/scripts/latlong.html
# That link also includes javascript for computing haversine distance.
# It should be straightforward to translate this to Python.
# Note the constant R in the equation controls the units of measure, and make sure you set it
# appropriately for meters as indicated in the docstring below.
# See documentation of Python's math functions for any needed trig functions as well as degree
# to radian conversion: https://docs.python.org/3/library/math.html
def haversine_distance(lat1, lng1, lat2, lng2) :
    """Computes haversine distance between two points in latitude, longitude.

    Keyword Arguments:
    lat1 -- latitude of point 1
    lng1 -- longitude of point 1
    lat2 -- latitude of point 2
    lng2 -- longitude of point 2

    Returns haversine distance in meters.
    """
    R = 6371000
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lng1 = math.radians(lng1)
    lng2 = math.radians(lng2)
    d_lat = lat2-lat1
    d_lng = lng2-lng1

    a = math.sin(d_lat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(d_lng/2)**2
    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    return R*c

# 4) Implement this function.  First note the lack of indentation.  This is not a method of the above class.
# It is a function.
#
# Specifically, it should be able to parse a file of the format from this set of graphs: http://tm.teresco.org/graphs/
# Details of the format itself can be found here: http://courses.teresco.org/metal/graph-formats.shtml
# Only worry about the "simple" format (and NOT the "collapsed" format).
# You might start by looking at one of the smaller graphs to see what the format looks like, such as Andora.
# First line of all files is: TMG 1.0 simple
# Second line tells you number of vertices and number of edges: V E
# The next V lines provide one vertex per line of the form: StringID  latitude  longitude
# You only really need the latitude and longitude values, and simply use 0 to V-1 as the vertex ids instead of the given
# strings.
# The next E lines provide the edges, one per line, of the form: from to aValueYouDontNeedForThisAssignment.
# You only need the from and to values, and not the 3rd value on the line.
# The from and to tell you the endpoints of an edge (0 based indices into the list of vertices).
# For each edge in this list add two directed edges to the WeightedAdjacencyMatrix (one in each direction).
# The weight for the edge should be the so-called haversine distance (which you implemented a function to
# compute in Step 3.
#
# HINTS (for parsing input file):
# You can find Python file IO examples here: https://docs.python.org/3/tutorial/inputoutput.html
# Scroll to 7.2 and look at examples of open. Specifically, see example that uses "with" which
# has the advantage that Python will automatically close the file for you at the end of the with block.
#
# The call to read() in that example, however, reads the entire file at once as a String.
# You will find it useful, to instead iterate over the lines of the file.  You can either use the readline
# method directly for this.  Or, see the example on that same page that uses a loop of the form:
# for line in f (each iteration of this loop will automatically call readline to get the next line of
# the file and loop will iterate over entire file).
#
# Useful methods for parsing the input graph file:
# The split method for Strings: https://docs.python.org/3/library/stdtypes.html#string-methods
#
# Converting String that is a number to a number type:
# float(s) will convert a string s that contains a floating-point number to a floating point number.
# For example, 
# s = "101.25"  # s is a string that happens to look like a floating-point number.
# v = float(s)  # v will now have the floating-point value 101.25
# Likewise, int(s) will do the same but for integer values.
#
def parse_highway_graph_data(filename) :
    """Parses a highway graph file and returns a WeightedAdjacencyMatrix.

    Keyword arguments:
    filename -- name of the file.

    Returns a WeightedAdjacencyMatrix object.
    """
    tmg = open(filename)
    tmg.readline()
    V,E = tmg.readline().split()
    V = int(V)
    E = int(E)

    #save the lat and lng of each vertex in order 
    vertex_values = list()
    for i in range(V):
        vert_id, lat, lng = tmg.readline().split()
        vertex_values.append((float(lat),float(lng)))
    
    # construct graph and add each edge in the file
    G = WeightedAdjacencyMatrix(V)
    for i in range(E):
        from_v,to_v,vert_id = tmg.readline().split()
        from_v = int(from_v)
        to_v = int(to_v)
        dist = haversine_distance(vertex_values[from_v][0],
            vertex_values[from_v][1],
            vertex_values[to_v][0],
            vertex_values[to_v][1])

        #add edges going both ways 
        G.add_edge(from_v,to_v,dist)
        G.add_edge(to_v,from_v,dist)
    tmg.close()
    return G


# 6a) This function should construct a WeightedAdjacencyMatrix object with the vertices and edges of your choice
# (small enough that you can verify that your Floyd Warshall implementation is correct).
# After constructing the WeightedAdjacencyMatrix object, call your floyd_warshall method, and then
# output the D matrix it returns using print statements (one row of matrix per line, columns separated by tabs).
# If you also computed the predecessor matrix, then output that as well (print a blank line between the matrices).
def test_with_your_own_graphs() :

    G = WeightedAdjacencyMatrix(4)
    G.add_edge(0,1,2)
    G.add_edge(1,3,2)
    G.add_edge(0,3,2)
    G.add_edge(2,3,2)
    G.add_edge(3,0,-1)
    D = G.floyd_warshall()

    for line in D[0]:
        for item in line:
            print(item,end="\t")
        print()
    print()
    for line in D[1]:
        for item in line:
            print(item,end="\t")
        print()

# 6b) This function should use your parseHighwayGraphData to get a WeightedAdjacencyMatrix object corresponding
# to the graph of your choice from http://tm.teresco.org/graphs/ (I recommend starting with one of the small graphs).
# Then use your floyd_warshall method to compute all pairs shortest paths.
# Don't output the entire matrix since that would be a bit large (even for the smaller graphs).
# Instead, the parameter to the function below is a list of 2-tuples.  For each 2-tuple, of the form (from, to)
# in this list, print on one line (in this order): from to distance
# If you implemented the extra credit part (the predecessors), then each line of output should be of the form:
# from to distance pathTaken
# You should do this with at least one graph from the linked site, but I recommend trying it with multiple.
# In what you submit, have this function work with one graph (of your choice).
# Upload that graph when you submit your assignment (in case the page updates the data, this way I'll have the exact
# graph that you used).
def test_with_highway_graph(L) :

    def path(P,from_v,to_v):
        by_v = P[from_v][to_v]
        if(by_v == to_v):
            print(to_v)
        else:
            print(by_v,end=" > ")
            path(P,by_v,to_v)

    if __name__=="__main__":
        G = parse_highway_graph_data(sys.argv[1])
    else:
        G = parse_highway_graph_data("AND-region-simple.tmg")

    D,P = G.floyd_warshall()
    for points in L:
        print(points)
        print(D[points[0]][points[1]],end="\t")
        print("Path: "+str(points[0]),end=" > ")
        path(P,points[0],points[1])


    print()


if __name__=="__main__":

    #arguments passed in the form :
    #   p4.py "relative/path/to/tmg" "from,to" "from,to" ... 
    L = list()
    for points in sys.argv[2:]:
        L.append([int(x) for x in points.split(",")])
    test_with_highway_graph(L)