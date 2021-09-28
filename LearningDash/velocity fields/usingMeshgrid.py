# -*- coding: utf-8 -*- (bbedit)

import numpy as np
import matplotlib.pyplot as plt

## FUNCTION DEFS



## "MAIN"

# create a meshgrid for our domain
x = np.linspace(-1, 1, 11)
y = np.linspace(-1, 1, 11)
xx, yy = np.meshgrid(x, y)

# example define a function of this domain
z = xx**2 + yy**2


# then we can display this plot in e.g. pyplot
h = plt.contourf(x, y, z)
plt.axis('scaled')
plt.show()

# so much cleaner

# So to implement the entirety of constant.py

x = np.linspace(-3, 3, 11)
y = np.linspace(-3, 3, 11)
xx, yy = np.meshgrid(x, y)

v1 = 0*xx + 1
v2 = 0*xx + 2


print (v1)
print (v2)
