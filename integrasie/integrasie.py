#%% Wys hoe werk scipy numeriese integrasie

from scipy.integrate import quad
from math import *
import numpy as np
from matplotlib import pyplot as plt

#%%

def integrand(x):
    return ((x**3) * np.cos(x/2) + 0.5)*(4 - x**2)**0.5


#%%

I = quad(integrand, -2, 2)

print(I[0]-I[1])
# %%
# Visualiseer die funksie deur dit te plot

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
x = np.linspace(-10, 2, 1000)


#%%

plt.plot(x, integrand(x), color='red')

plt.show()

# %%
