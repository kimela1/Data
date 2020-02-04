#!/usr/bin/env python
# coding: utf-8

# # Plotting Practice

# #### Necessary imports

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ## Gas Prices

# Create line graphs of global gas price data over time. Add a title, x & y axis labels, and scale the graphs. Customize the style and size of the charts. 

# #### Load data

# In[2]:


gas = pd.read_csv('gas_prices.csv')

gas


# #### Line Graph

# In[3]:


plt.figure(figsize=(8,5))

plt.title('Gas Prices over Time (in USD)', fontdict={'fontweight':'bold', 'fontsize':16})

plt.plot(gas.Year, gas.USA, 'b.-', label='United States')
plt.plot(gas.Year, gas.Canada, 'r.-', label='Canada')
plt.plot(gas.Year, gas['South Korea'], 'g.-', label='South Korea')
plt.plot(gas.Year, gas.Australia, 'y.-', label='Australia')

#for country in gas:
#    if country != 'Year':
#        plt.plot(gas.Year, gas[country], marker='.')

plt.xticks(gas.Year[::2])

plt.xlabel('Year')
plt.ylabel('US Dollars ($)')

plt.legend()

plt.savefig('Gas_price_figure.png', dpi=300)

plt.show()


#  

# ## Fifa Data

# Look at the FIFA 19 player data to create a histogram, a couple pie charts, and a box and whisker plot.
# Data from [Kaggle](https://www.kaggle.com/karangadiya/fifa19)

# #### Load data

# In[4]:


fifa = pd.read_csv('fifa_data.csv')

fifa.head()


# #### Histogram

# In[5]:


bins = [30,40,50,60,70,80,90,100] # setting intervals

plt.hist(fifa.Overall, bins=bins, color='#f0a665')

plt.xticks(bins)

plt.title('Distribution of Player Skills in FIFA 2018')
plt.xlabel('Skill Level')
plt.ylabel('Number of Players')

plt.show()


# #### Pie Charts

# In[6]:


left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

labels = ['Left', 'Right']
colors = ['#c5e0ab','#efdaff']

plt.pie([left,right], labels=labels, colors=colors, autopct='%.2f%%')

plt.title('Preferred Foot of FIFA Players', fontdict={'fontweight':'bold', 'fontsize':16})

plt.show()


# In[7]:


plt.style.use('seaborn-pastel')

# convert numbers in weight string to int
fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]

# set conditions
light = fifa.loc[(fifa.Weight < 125)].count()[0]
light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
medium = fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
heavy = fifa.loc[(fifa.Weight >= 200)].count()[0]

weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ['Under 125', '125-149', '150-174', '175-199', '200+']
explode = (.4, .2, 0, 0, .4)

plt.pie(weights, labels=labels, autopct='%.2f%%', pctdistance=0.8, explode=explode)

plt.title('Weight Distribution of FIFA Players', fontdict={'fontweight':'bold', 'fontsize':16})

plt.show()


# #### Box and Whisker Plot

# In[14]:


plt.figure(figsize=(5,8), dpi=100)

plt.style.use('default')

pohang = fifa.loc[fifa.Club == "Pohang Steelers"]['Overall']
daegu = fifa.loc[fifa.Club == "Daegu FC"]['Overall']
seoul = fifa.loc[fifa.Club == "FC Seoul"]['Overall']

bp = plt.boxplot([pohang, daegu, seoul], labels=['Pohang Steelers','Daegu FC','FC Seoul'], patch_artist=True, medianprops={'linewidth': 2})

plt.title('Professional Soccer Team Comparison')
plt.ylabel('FIFA Overall Rating')

for box in bp['boxes']:
    box.set(color='#4286f4', linewidth=2) # outline color
    box.set(facecolor = '#e0e0e0' ) # fill color
    
plt.show()


# In[ ]:




