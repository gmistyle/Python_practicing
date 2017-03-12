import matplotlib.pyplot as plt
plt.plot(x, y) #line plot
plt.scatter(x, y) #scatter plot
plt.hist(data) #histogram
plt.xscale('log') #logarithmic scale
plt.show() #display a plot

# If you combo the code between plt.hist(a) and plt.hist(b)
# It will show both histograms on the same page

plt.clf() #cleans it up again so you can start afresh.

# Add axis labels
plt.xlabel('xlab')
plt.ylabel('ylab')

# Add title
plt.title('title')

# Definition of tick_val and tick_lab
tick_val = [1000,10000,100000] #plot will place dots according to this rule
tick_lab = ['1k','10k','100k'] #and it will show the label on the plot 

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# argument s, for size.
# size can be corresponds to the data 
# It will be like a bubble plot
plt.scatter(gdp_cap, life_exp, s = pop)

# argument c, for color.
plt.scatter(gdp_cap, life_exp, s = pop, c = col)

# Change the opacity of the bubbles by setting the alpha argument to 0.8 inside plt.scatter(). 
# Alpha can be set from zero to one, where zero totally transparant, and one is not transparant.
plt.scatter(gdp_cap, life_exp, s = pop, c = col, alpha = 0.8)
