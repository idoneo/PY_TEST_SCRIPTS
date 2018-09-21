#https://python-graph-gallery.com/125-small-multiples-for-line-chart/
# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Make a data frame
df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14), 'y9': np.random.randn(10)+range(4,14) })

# Initialize the figure
plt.style.use('seaborn-darkgrid')

# create a color palette
palette = plt.get_cmap('Set1')

# multiple line plot
num=0
for column in df.drop('x', axis=1):
	num+=1

	# Find the right spot on the plot
	plt.subplot(3,3, num)

	# Plot the lineplot
	plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=1.9, alpha=0.9, label=column)

	# Same limits for everybody!
	plt.xlim(0,10)
	plt.ylim(-2,22)

	# Not ticks everywhere
	if num in range(7) :
		plt.tick_params(labelbottom='off')
	if num not in [1,4,7] :
		plt.tick_params(labelleft='off')

	# Add title
	plt.title(column, loc='left', fontsize=12, fontweight=0, color=palette(num) )

# general title
plt.suptitle("How the 9 students improved\nthese past few days?", fontsize=13, fontweight=0, color='black', style='italic', y=1.02)

# Axis title
plt.text(0.5, 0.02, 'Time', ha='center', va='center')
plt.text(0.06, 0.5, 'Note', ha='center', va='center', rotation='vertical')



#SAME with greyed out lines in background
# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Make a data frame
df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14), 'y9': np.random.randn(10)+range(4,14) })

# Initialize the figure
plt.style.use('seaborn-darkgrid')

# create a color palette
palette = plt.get_cmap('Set1')

# multiple line plot
num=0
for column in df.drop('x', axis=1):
	num+=1

	# Find the right spot on the plot
	plt.subplot(3,3, num)

	# plot every groups, but discreet
	for v in df.drop('x', axis=1):
		plt.plot(df['x'], df[v], marker='', color='grey', linewidth=0.6, alpha=0.3)

	# Plot the lineplot
	plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=2.4, alpha=0.9, label=column)

	# Same limits for everybody!
	plt.xlim(0,10)
	plt.ylim(-2,22)

	# Not ticks everywhere
	if num in range(7) :
		plt.tick_params(labelbottom='off')
	if num not in [1,4,7] :
		plt.tick_params(labelleft='off')

	# Add title
	plt.title(column, loc='left', fontsize=12, fontweight=0, color=palette(num) )

# general title
plt.suptitle("How the 9 students improved\nthese past few days?", fontsize=13, fontweight=0, color='black', style='italic', y=1.02)

# Axis title
plt.text(0.5, 0.02, 'Time', ha='center', va='center')
plt.text(0.06, 0.5, 'Note', ha='center', va='center', rotation='vertical')

#SPAGETTI PLOT
# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Make a data frame
df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14), 'y9': np.random.randn(10)+range(4,14), 'y10': np.random.randn(10)+range(2,12) })

# style
plt.style.use('seaborn-darkgrid')

# create a color palette
palette = plt.get_cmap('Set1')

# multiple line plot
num=0
for column in df.drop('x', axis=1):
num+=1
plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=1, alpha=0.9, label=column)

# Add legend
plt.legend(loc=2, ncol=2)

# Add titles
plt.title("A (bad) Spaghetti plot", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("Time")
plt.ylabel("Score")

#HIGHLIGH 1 LINE
# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Make a data frame
df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14) })

#plt.style.use('fivethirtyeight')
plt.style.use('seaborn-darkgrid')
my_dpi=96
plt.figure(figsize=(480/my_dpi, 480/my_dpi), dpi=my_dpi)

# multiple line plot
for column in df.drop('x', axis=1):
   plt.plot(df['x'], df[column], marker='', color='grey', linewidth=1, alpha=0.4)

# Now re do the interesting curve, but biger with distinct color
plt.plot(df['x'], df['y5'], marker='', color='orange', linewidth=4, alpha=0.7)

# Change xlim
plt.xlim(0,12)

# Let's annotate the plot
num=0
for i in df.values[9][1:]:
   num+=1
   name=list(df)[num]
   if name != 'y5':
      plt.text(10.2, i, name, horizontalalignment='left', size='small', color='grey')

# And add a special annotation for the group we are interested in
plt.text(10.2, df.y5.tail(1), 'Mr Orange', horizontalalignment='left', size='small', color='orange')

# Add titles
plt.title("Evolution of Mr Orange vs other students", loc='left', fontsize=12, fontweight=0, color='orange')
plt.xlabel("Time")
plt.ylabel("Score")


#AREA WITH FACET
# libraries
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a dataset
my_count=["France","Australia","Japan","USA","Germany","Congo","China","England","Spain","Greece","Marocco","South Africa","Indonesia","Peru","Chili","Brazil"]
df = pd.DataFrame({
"country":np.repeat(my_count, 10),
"years":range(2000, 2010) * 16,
"value":np.random.rand(160)
})

# Create a grid : initialize it
g = sns.FacetGrid(df, col='country', hue='country', col_wrap=4, )

# Add the line over the area with the plot function
g = g.map(plt.plot, 'years', 'value')

# Fill the area with fill_between
g = g.map(plt.fill_between, 'years', 'value', alpha=0.2).set_titles("{col_name} country")

# Control the title of each facet
g = g.set_titles("{col_name}")

# Add a title for the whole plo
plt.subplots_adjust(top=0.92)
g = g.fig.suptitle('Evolution of the value of stuff in 16 countries')

plot.show()


#IMPROVE AREAS CHARTS 
"""
The chart #240 describes how to make a basic area chart. 
This page aims to describe a few customisation you can apply to your area chart. 
It is highly advised to change the default colour of matplotlib. Moreover, it
is quite common to use a color with transparency, and add a line with a stronger colour on the top of the area.
These 2 elements are drawn using 2 lines of code, one for the area (fill_between), and one for the line (plot)."""
# library
import numpy as np
import matplotlib.pyplot as plt

# create data
x=range(1,15)
y=[1,4,6,8,4,5,3,2,4,1,5,6,8,7]

# Change the color and its transparency
plt.fill_between( x, y, color="skyblue", alpha=0.4)
plt.show()

# Same, but add a stronger line on top (edge)
plt.fill_between( x, y, color="skyblue", alpha=0.2)
plt.plot(x, y, color="Slateblue", alpha=0.6)
# See the line plot function to learn how to customize the plt.plot function


# get seaborn
import seaborn as sns

# Make the same graph
plt.fill_between( x, y, color="skyblue", alpha=0.3)
plt.plot(x, y, color="skyblue")

# Add titles
plt.title("An area chart", loc="left")
plt.xlabel("Value of X")
plt.ylabel("Value of Y")

