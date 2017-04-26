import scipy
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy


x0 = np.arange(10)
y0 = [math.sin(i) for i in x0]

points = zip(x0, y0)
points = sorted(points, key=lambda point: point[0])

x0, y0 = zip(*points)


fig = plt.figure()
ax = fig.add_subplot(111)

plt.grid(linestyle="-", color=(0.7, 0.8, 1.0))

plt.plot(x0, y0, 'o', label='Data', markersize=8)

# Array with points in between those of the data set for interpolation.
x = np.linspace(min(x0), max(x0), 1000)

xvalues = list(x0)
yvalues = list(y0)

newx = 0.0
newxval = []
newyval = []
newxval.append(min(x0))
for i, val in enumerate(xvalues):

    print newx

    if i < len(xvalues)-1:

        newx = ((xvalues[i + 1] - xvalues[i]) / 2.) + xvalues[i]
    else:
        newx = max(x0)

    newxval.append(newx)
    newxval.append(newx)

    newyval.append(yvalues[i])
    newyval.append(yvalues[i])

    print newx




newyval.append(max(y0))

plt.plot(x0, y0, label='linear', linewidth=1.5, c='r')
plt.plot(newxval, newyval, label='nearest', linewidth=1.5, c='y')


result = scipy.poly1d([0.0])  # setting result = 0

for i in range(0, len(x0)):  # number of polynomials L_k(x).
    temp_numerator = scipy.poly1d([1.0])  # resets temp_numerator such that a new numerator can be created for each i.
    denumerator = 1.0  # resets denumerator such that a new denumerator can be created for each i.
    for j in range(0, len(x0)):
        if i != j:
            temp_numerator *= scipy.poly1d([1.0, -x0[j]])  # finds numerator for L_i
            denumerator *= x0[i] - x0[j]  # finds denumerator for L_i
    result += (temp_numerator / denumerator) * y0[i]  # linear combination

x_val = np.arange(min(x0), max(x0)+0.1, 0.1)  # generates x values we would like to evaluate.
plt.plot(x_val, result(x_val), label='Lagrange', linewidth=1.5, c='b')  # result(x_val) gives the value of our Lagrange polynomial.

ax.set_xlabel('Wartosci $x$', fontsize=23)
ax.set_ylabel('Interpolacja wartosci $y$', fontsize=23)

plt.legend(loc='lower left')
plt.show()








