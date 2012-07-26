
import pyDatalog # or from pyDatalog import pyDatalog
import time

# with more memoization

pyDatalog.clear()
@pyDatalog.program()
def _():
    queens0(X0) <= (X0 in range(8))

    # when is it ok to have a queen in row X1 and another in row X2, separated by N columns
    # this is memoized !
    ok(X1, N, X2) <= (X1!=X2) & (X1!= X2+N) & (X1!=X2-N)
    
    queens1(X0,X1) <= queens0(X0) & (X1 in range(8)) & ok(X1,1,X0)

    queens2(X0,X1,X2) <= queens1(X0,X1) & (X2 in range(8)) & ok(X2, 1, X1, X0)
    # when is it ok to have 2 queens N columns away from another one ?  Also memoized
    ok(X2, N, X1, X0) <= ok(X2,N,X1) & (N1==N+1) & ok(X2,N1,X0)

    queens3(X0,X1,X2,X3) <= queens2(X0,X1,X2) & (X3 in range(8))  & ok(X3, 1, X2, X1, X0)
    ok(X3, N, X2, X1, X0) <= ok(X3,N, X2,X1)& (N1==N+2) & ok(X3,N1,X0)

    queens4(X0,X1,X2,X3,X4) <= queens3(X0,X1,X2,X3) & (X4 in range(8)) & ok(X4,1, X3, X2, X1) & ok(X4,4,X0)

    queens5(X0,X1,X2,X3,X4,X5) <= queens4(X0,X1,X2,X3,X4) & (X5 in range(8)) & ok(X5,1,X4,X3,X2) & ok(X5,4,X1,X0)

    queens6(X0,X1,X2,X3,X4,X5,X6) <= queens5(X0,X1,X2,X3,X4,X5) & (X6 in range(8)) & ok(X6,1,X5,X4,X3) & ok(X6,4,X2,X1,X0)
    # counting is 0-based, so this is actually the 8-queens solution
    queens7(X0,X1,X2,X3,X4,X5,X6,X7) <= queens6(X0,X1,X2,X3,X4,X5,X6) & (X7 in range(8)) & ok(X7,1,X6,X5,X4) & ok(X7,4,X3,X2,X1) & ok(X7,7,X0)

# counting is 0-based, so this is actually the 8-queens solution
print(pyDatalog.ask("queens7(X0,X1,X2,X3,X4,X5,X6,X7)"))
    
# there is a fixed penalty the first time around (JIT, ...), so let's measure performance the second time
start_time = time.time()
datalog_count = len(pyDatalog.ask("queens7(X0,X1,X2,X3,X4,X5,X6,X7)").answers)
datalog_time = (time.time() - start_time)

# pure python solution found on http://rosettacode.org/wiki/N-Queens#Python, for comparison purposes

from itertools import permutations

start_time = time.time()
 
n = 8
cols = range(n)
for vec in permutations(cols):
    if n == len(set(vec[i]+i for i in cols)) \
         == len(set(vec[i]-i for i in cols)):
        #print ( vec )
        pass
python_time = time.time() - start_time

print("%i solutions by datalog in %f seconds" % (datalog_count, datalog_time))
print("python : %f seconds" % python_time)