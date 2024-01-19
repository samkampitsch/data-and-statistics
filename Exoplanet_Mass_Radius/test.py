import numpy as np
from matplotlib import pyplot as plt
from astropy.io import ascii, fits

table = ascii.read("exoplanet.eu_catalog.dat", format="tab")
print(table)
mass = table["mass"]
radius = table["radius"]
mask = (mass>0) * (radius>0)

plt.plot(mass[mask], radius[mask], "o")
plt.semilogx()
plt.show()
