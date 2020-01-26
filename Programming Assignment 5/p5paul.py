# Programming Assignment 5
#
# Don't rename any functions, although feel free to implement any helper functions
# you find useful.
#
# 1) Implement the naive_string_matcher function as specified in its docstring.
#    This is a variation of the algorithm on page 988 of the textbook.
#    Read the docstring below carefully so you know what I've changed.
#
# 2) Implement the function print_results below.
#
# 3) Implement the p_naive_string_matcher function as specified in its docstring.
#
# 4) In the time_results function below, implement any code needed to compare the runtimes
#    of the sequential and parallel version on string of varying lengths.  You will need to
#    figure out how to generate strings of varying lengths.  Here's one approach to get a really
#    long string to use as T (long enough that you will almost certainly see a benefit to parallel
#    implementation.  The complete works of shakespeare is freely available (http://shakespeare.mit.edu/ among
#    other places).  You might just hardcode a long string by copying and pasting and surrounding with """ and """
#    to get a multiline string.
#
# 5) Answer the following questions here in a comment based on #4:
#
#    Q1: After running time_results, fill in this table in this comment for whatever P and T lengths
#        you tried (make sure you vary lengths from short to longer:
#        T-length                 P-Length                  Sequential                Parallel
#         75015                      51                 5.244828689                0.5198740080000004
#          3535                     505                 0.026436074000000254       0.22709064599999973
#        250010                   50010                 1.8765912390000006         1.1345575299999995
#       1007903                   16008                 7.666404766000001          4.920288195000001
#       1250005                 1250005                 1.7773290260000003         0.5478145010000013
#
#    Q2: How do the times (of both versions) vary by string length?  If T is held constant, and pattern P length varied, how does
#        that affect runtime?  If P length is held constant, and text T length varied, how does that affect runtimes?
#
#
#           As Text length got larger the runtime increased proportionally
#           As Pattern length got larger the runtime increased proportionally. This Runtime increase was not as bad as the increase from Text Length
#
#
#    Q3: At what lengths of P and/or T is the sequential version faster?
#
#       For my run times when the Text and Patterns length were smaller, Sequential time was faster.
#
#    Q4: At what lengths of P and/or T is the parallel version faster?
#       For my run times as the Text and Pattern length got larger, Parallel time was faster. I think this is because the processes have startup times. A good specific example is runtime 5 which had about a second faster run time compared to sequential.
#    Q5: Are the results consistent with the speedup you computed in Problem Set 4?  If not, what do you think caused
#        the inconsistency with the theoretical speedup?
#       These results are inconsistent to what we got in problem set 4. As discussed in class, it costs time to add a processor where as in problem set we discussed P should be linear speed up.

# These are imports you will likely need.  Feel free to add any other imports that are necessary.
# E.g., you might also need Queue for getting the results back from your processes.
import multiprocessing 
import timeit
from functools import partial


def time_results():
    """Write any code needed to compare the timing of the sequential and parallel versions
    with a variety of string lengths."""
    def parallel_Time(T, P):
        """Uses timeit to time the parallel run time of any T and P. Returns the time."""
        time = timeit.timeit(lambda: p_naive_string_matcher(T, P), number=10)
        return time

    def sequential_Time(T, P):
        time = timeit.timeit(lambda: naive_string_matcher(T, P), number=10)
        return time

    def increase_T(T, amount):
        Tcopy = T
        for i in range(amount):
            Tcopy += T * 5
        return Tcopy

    if __name__ == "__main__":
        trial1_increased = increase_T(trial1_Text, 1000)
        trial1_increased_pattern = increase_T(trial1_Pattern,10)
        trial1_sequential = sequential_Time(trial1_increased, trial1_increased_pattern)
        trial1_parallel = parallel_Time(trial1_increased, trial1_increased_pattern)

        trial2_increased = increase_T(trial2_Text, 20)
        trial2_increased_pattern = increase_T(trial2_Pattern,20)
        trial2_sequential = sequential_Time(trial2_increased, trial2_increased_pattern)
        trial2_parallel = parallel_Time(trial2_increased, trial2_increased_pattern)

        trial3_increased = increase_T(trial3_Text, 5000)
        trial3_increased_pattern = increase_T(trial3_Pattern,1000)
        trial3_sequential = sequential_Time(trial3_increased, trial2_increased_pattern)
        trial3_parallel = parallel_Time(trial3_increased, trial2_increased_pattern)
        trial4_increased = increase_T(trial4_Text, 500)
        trial4_increased_pattern = increase_T(trial4_Pattern,400)
        trial4_sequential = sequential_Time(trial4_increased, trial4_increased_pattern)
        trial4_parallel = parallel_Time(trial4_increased, trial4_increased_pattern)
        trial5_increased = increase_T(trial5_Text, 50000)
        trial5_increased_pattern = increase_T(trial5_Pattern,50000)
        trial5_sequential = sequential_Time(trial5_increased, trial5_increased_pattern)
        trial5_parallel = parallel_Time(trial5_increased, trial5_increased_pattern)

        print('{:^20} {:^20} {:^30} {:^20}'.format("Text Length", "String Length", "Sequential Time", "Parallel Time"))
        print('{:^15} {:^25} {:^30} {:^10}'.format(len(trial1_increased), len(trial1_increased_pattern), trial1_sequential, trial1_parallel))
        print('{:^15} {:^25} {:^30} {:^10}'.format(len(trial2_increased), len(trial2_increased_pattern), trial2_sequential, trial2_parallel))

        print('{:^15} {:^25} {:^30} {:^10}'.format(len(trial3_increased), len(trial3_increased_pattern), trial3_sequential, trial3_parallel))

        print('{:^15} {:^25} {:^30} {:^10}'.format(len(trial4_increased), len(trial4_increased_pattern), trial4_sequential, trial4_parallel))

        print('{:^15} {:^25} {:^30} {:^10}'.format(len(trial5_increased), len(trial5_increased_pattern), trial5_sequential, trial5_parallel))


def print_results(L):
    """Prints the list of indices for the matches."""
    for i in L:
        print(i,end="  ")
    print()


def naive_string_matcher(T, P):
    """Naive string matcher algorithm from textbook page 988.

    Slight variation of the naive string matcher algorithm from
    textbook page 988.  Specifically, the textbook version prints the
    results.  This python function does not print the results.
    Instead, it generates and returns a list of the indices at the start
    of each match.  For example, if T="abcabcabc" and P="def", this function
    will return the empty list [] since the pattern doesn't appear in T.
    For that same T, if the pattern P="abc", then this function will return
    the list [0, 3, 6] since the pattern appears 3 times, beginning on indices
    0, 3, and 6.

    Keyword arguments:
    T -- the text string to search for patterns.
    P -- the pattern string.
    """

    output = list()
    for i in range((len(T) - len(P) + 1)):
        for j in range(len(P)):
            if T[i + j] != P[j]:
                break
        if j == len(P) - 1:
            output.append(i)
    return output


def p_naive_string_matcher(T, P, p = 4):
    """Parallel naive string matcher algorithm from Problem Set 4.

    This function implements the parallel naive string matcher algorithm that you specified in
    Problem Set 4.  You may assume in your implementation that there are 4 processor cores.
    If you want to write this more generally, you may add a parameter to the function for number
    of processes.  If you do, don't change the order of the existing parameters, and your new parameters
    must follow, and must have default values such that if the only parameters I pass are T and P, that
    you default to 4 processes.

    Like the sequential implementation from step 1 of assignment, this function should not
    print results.  Instead, have it return a list of the indices where the matches begin.
    For example, if T="abcabcabc" and P="def", this function
    will return the empty list [] since the pattern doesn't appear in T.
    For that same T, if the pattern P="abc", then this function will return
    the list [0, 3, 6] since the pattern appears 3 times, beginning on indices
    0, 3, and 6.

    You must use Process objects (or a Pool of processes) from the multiprocessing module and not Threads from threading because
    in the next step of the assignment, you're going to investigate performance relative to the sequential
    implementation.  And due to Python's global interpreter lock, you won't see any gain if you use threads.

    You will need to decide how to distribute the work among the processes.
    One way (not the only way) is to give all of your processes T and P, and to give each process
    a range of starting indices to check, such that you give each approximately equal sized ranges.
    Another way is to give all processes the pattern string P, but only a substring of T (of approximately
    equal size).  In this case, you'd need to figure out how to map the indices back into the original.

    You will need to decide how to get the results back from the processes.
    One way (not the only way) is to give all processes a reference to a Queue object for the results.

    If you give all processes the full T and P, then if the size of the text T is large, the savings from
    multiprocessing may be outweighed by the cost of giving each its own independent copy of T.
    You might try using an Array object to use shared memory.  Here's how to do it.  Create an array of
    characters in shared memory with: a = Array(ctypes.c_wchar, "Hello World", lock=None)
    You'll need to import ctypes
    for this to work.  You can then access individual characters with a[0], a[1], etc.
    You might do this for both T and P.  None of the processes need to change them, so there is no risk
    of a race condition.

    An alternative to using Process objects directly is to use a Pool, and in particular to use the Pool.map
    method.  Hints to help you if you want to consider this approach: 1) You'll need a function of one argument
    to pass to Pool.map, and a list of the values for that argument.  This list can be a list of the starting indices
    to check for matches (i.e., the indices from the outer loop of the naive string matcher).  The one argument function's
    one argument can be the index to check, and can then check if a match starts at that index. 2) But wait, wouldn't that
    function need 3 arguments, T, P, and the index? Yes. Start by creating a helper function with those 3 arguments, with
    index as the last argument.  Your helper can simply return a boolean indicating whether it is a match.
    Then, look up the documentation for a function named partial in the Python module functools.
    partial takes as arguments a function and some of the arguments for it, and returns to you a function where those arguments
    will be passed by default.  E.g., you can pass your helper function, and T and P to partial, and it will return to you a
    function that you simply need to pass index (the remaining argument).  3) Your last hint.  If you follow hints 1 and 2, you'll
    end up with a list of booleans, true if that corresponding index was a match and false otherwise.  The final step would
    be to use that to generate what this string matcher is actually supposed to return.

    Keyword arguments:
    T -- the text string to search for patterns.
    P -- the pattern string.
    """
    start_list = []
    to_check = []
    match = []
    create_pool = multiprocessing.Pool()
    for i in range(len(T) - len(P) + 1):
        to_check.append(i)

    to_helper = partial(helper, T, P, len(P))

    for i in create_pool.map(to_helper, to_check):
        if i is not None:
            match.append(i)
    start_list.append(match)
    return match

def helper(T, P, p, i):
    if P == T[i:i + p]:
        return i


trial1_Text = "aaaaaaaaaaaaaaa"
trial1_Pattern = "a"
trial2_Text = "whatdowedowhentheworldstopsspinning"
trial2_Pattern = "world"
trial3_Text = "abcdefghij"
trial3_Pattern = "abcdefghij"
trial4_Text = """His sole child, my lord, and bequeathed to my
overlooking. I have those hopes of her good that
her education promises; her dispositions she
inherits, which makes fair gifts fairer; for where
an unclean mind carries virtuous qualities, there
commendations go with pity; they are virtues and
traitors too; in her they are the better for their
simpleness; she derives her honesty and achieves her goodness."""
trial4_Pattern = "promises"
trial5_Text = "abcde"
trial5_Pattern = "abcde"

time_results()




