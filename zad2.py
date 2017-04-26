import scipy
import matplotlib.pyplot as plt
import numpy as np
import math

x0 = np.arange(9)
y0 = [math.sin(i) for i in x0]


result = scipy.poly1d([0.0])  # setting result = 0

for i in range(0, len(x0)):  # number of polynomials L_k(x).
    temp_numerator = scipy.poly1d([1.0])  # resets temp_numerator such that a new numerator can be created for each i.
    denumerator = 1.0  # resets denumerator such that a new denumerator can be created for each i.
    for j in range(0, len(x0)):
        if i != j:
            temp_numerator *= scipy.poly1d([1.0, -x0[j]])  # finds numerator for L_i
            denumerator *= x0[i] - x0[j]  # finds denumerator for L_i
    result += (temp_numerator / denumerator) * y0[i]  # linear combination

print("The result is: ")
print(result)


x_val = np.arange(min(x0), max(x0) + 1, 0.1)  # generates x values we would like to evaluate.
plt.xlabel('x');
plt.ylabel('p(x)')
plt.grid(True)


plt.plot(x_val, result(x_val))  # result(x_val) gives the value of our Lagrange polynomial.

plt.axis([min(x0) - 1, max(x0) + 1, min(y0) - 1, max(y0) + 1])
plt.show()
