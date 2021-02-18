from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(size=1000)
hist, bins = np.histogram(data, bins=20)

#bin_midpoints = bins[:-1] + np.diff(bins)/2
#cdf = np.cumsum(hist)
#cdf = cdf / cdf[-1]
#values = np.random.rand(10000)
#value_bins = np.searchsorted(cdf, values)
#random_from_cdf = bin_midpoints[value_bins]

plt.subplot(121)
plt.hist(data, 20)
#plt.subplot(122)
#splt.hist(random_from_cdf, 50)
plt.show()
