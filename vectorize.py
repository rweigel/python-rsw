# Based on
# https://towardsdatascience.com/data-science-with-python-turn-your-conditional-loops-to-numpy-vectors-9484ff9c622e
# with the addition of use of np.asarray(condition).nonzero().

import numpy as np
import time

# Number of test points
N_point  = 1000

# Define a custom function with some if-else loops
def myfunc(x,y):
    if x > 0.5*y and y < 0.3:
        return x-y
    elif x < 0.5*y:
        return 0
    elif (x>0.2*y):
        return 2*x+2*y
    else:
        return y+x

lst_x = np.random.randn(N_point)
lst_y = np.random.randn(N_point)
lst_result = []

# for loop
tic = time.time()
for j in range(1000):
    for i in range(len(lst_x)):
        lst_result.append(myfunc(lst_x[i], lst_y[i]))
toc = time.time()
print("for loop: %.2f s" % (toc-tic))

# List comprehension
tic = time.time()
for i in range(1000):
    lst_result = [myfunc(x,y) for x,y in zip(lst_x,lst_y)]
toc = time.time()
print("list comprehension: %.2f s" % (toc-tic))

# map() function
tic = time.time()
for i in range(1000):
    list(map(myfunc,lst_x,lst_y))
toc = time.time()
print("map function: %.2f s" % (toc-tic))

# numpy.vectorize
tic = time.time()
vectfunc = np.vectorize(myfunc,otypes=[np.float],cache=False)
for i in range(1000):
    list(vectfunc(lst_x,lst_y))
toc = time.time()
print("numpy.vectorize method: %.2f s" % (toc-tic))

tic = time.time()
x = np.random.randn(N_point)
y = np.random.randn(N_point)
for i in range(1000):
    z = (y+x)*np.ones(N_point) # Fall-through case
    #idx = np.where(np.all([x > 0.5*y, y<0.3]))[0]
    idx = np.asarray(np.all([x > 0.5*y, y<0.3], axis=0)).nonzero()
    z[idx] = x[idx]-y[idx]
    #idx = np.where(x < 0.5*y)[0]
    idx = np.asarray(x < 0.5*y).nonzero()
    z[idx] = x[idx]-y[idx]
    #idx = np.where(x > 0.2*y)[0]
    idx = np.asarray(x > 0.2*y).nonzero()
    z[idx] = x[idx]-y[idx]
toc = time.time()
print("np.where method: %.3f s" % (toc-tic))

# Results
"""
for loop: 0.81 s
list comprehension: 0.63 s
map function: 0.55 s
numpy.vectorize method: 0.29 s
np.where method: 0.040 s
"""