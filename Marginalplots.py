# library & dataset
import seaborn as sns
df = sns.load_dataset('iris')

# Custom the inside plot: options are: “scatter” | “reg” | “resid” | “kde” | “hex”
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='scatter')
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='hex')
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='kde')
# Then you can pass arguments to each type:
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='scatter', s=200, color='m', edgecolor="skyblue", linewidth=2)

# Custom the color
sns.set(style="white", color_codes=True)
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='kde', color="skyblue")

# library & dataset
import seaborn as sns
df = sns.load_dataset('iris')
 
# HEXbin Custom the histogram and add rug:
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='hex', marginal_kws=dict(bins=30, rug=True))


#KDE
# library & dataset
import seaborn as sns
df = sns.load_dataset('iris')

# No space marginal info on top if axes
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='kde', color="grey", space=0)

# Huge space marginal info floats above axis
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='kde', color="grey", space=3)

# Make marginal bigger:
sns.jointplot(x=df["sepal_length"], y=df["sepal_width"], kind='kde',ratio=1)

#DENSITY PLOT
# libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kde

# create data
x = np.random.normal(size=500)
y = x * 3 + np.random.normal(size=500)

# Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
nbins=300
k = kde.gaussian_kde([x,y])
xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))

# Make the plot
plt.pcolormesh(xi, yi, zi.reshape(xi.shape))
plt.show()

# Change color palette
plt.pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=plt.cm.Greens_r)
plt.show()
# Add color bar
plt.pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=plt.cm.Greens_r)
plt.colorbar()
plt.show()