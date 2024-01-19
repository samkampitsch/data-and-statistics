import numpy as np
from matplotlib import pyplot as plt
from astropy.io import ascii



table = ascii.read("Radio Fluxes.dat", format="tab")

tbl = ascii.read("Radio Fluxes.dat")
tbl
