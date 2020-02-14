#!/usr/bin/env python
# coding: utf-8

# # Sales Analysis

# Using Python Pandas & Python Matplotlib to analyze and answer business questions about 12 months worth of sales data The data contains hundreds of thousands of electronics store purchases broken down by month, product type, cost, purchase address, etc.

# In[1]:


import pandas as pd
import os


# ## Fetching data

# #### Merge 12 months of sales data into a single CSV file

# In[2]:


df = pd.read_csv('./Sales_Data/Sales_April_2019.csv')

files = [file for file in os.listdir('./Sales_Data')]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv('./Sales_Data/'+file)
    all_months_data = pd.concat([all_months_data, df])

all_months_data.to_csv("all_data.csv", index=False)


# #### Read in Data

# In[3]:


all_data = pd.read_csv("all_data.csv")
all_data.head()


# ## Data Cleaning

# #### Drop rows with NaN and reset index

# In[4]:


nan_df = all_data[all_data.isna().any(axis=1)]

all_data = all_data.dropna(how='all')

all_data.reset_index(drop=True, inplace=True)
all_data.head()


# #### Find 'Or' and delete it

# In[5]:


all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']


# #### Convert columns to correct data type

# In[6]:


all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered']) # Make int
all_data['Price Each'] = pd.to_numeric(all_data['Price Each']) # Make float


# #### Add month column

# In[7]:


all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')
all_data.head()


# #### Add a sales column

# In[8]:


all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
all_data.head()


# #### Add a city column

# In[9]:


# Use .apply()
def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]
    
all_data['Purchase City'] = all_data['Purchase Address'].apply(lambda x: get_city(x) + ' (' + get_state(x) + ')')

all_data.head()


# ## Exploratory Data Analysis

# ### Which month had the most sales? How much was earned that month?

# In[10]:


results = all_data.groupby('Month').sum()
results


# #### Plot data

# In[11]:


import matplotlib.pyplot as plt

months = range(1, 13)

plt.bar(months, results['Sales'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month')
plt.show()


# Interpreting the results:
# * December has the most sales (most likely because of the holidays).
# * The store earned $4,613,443 in December.

# ### Which city had the highest number of sales?

# In[12]:


results = all_data.groupby('Purchase City').sum()
results


# #### Plot data

# In[13]:


import matplotlib.pyplot as plt

cities = [city for city, df in all_data.groupby('Purchase City')]

plt.bar(cities, results['Sales'])
plt.xticks(cities, rotation='vertical', size=8)
plt.ylabel('Sales in USD ($)')
plt.xlabel('City name')
plt.show()


# Interpreting the results:
# * San Francisco, CA has the highest number of sales.
# * There were 8,262,204 sales in San Francisco.

# ### What is the best time to display advertisements to maximize the likelihood of customers buying product?

# In[14]:


# Convert order date to date time object
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])


# In[15]:


all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute
all_data.head()


# #### Plot data

# In[25]:


hours = [hour for hour, df in all_data.groupby('Hour')]

plt.plot(hours, all_data.groupby(['Hour']).count())
plt.xticks(hours)
plt.ylabel('Number of Orders')
plt.xlabel('Time (Hour)')
plt.grid()
plt.show()


# Interpreting the results:
# * There are peaks at around 11:00 and 19:00.
# * The best time to display advertisements would be around 11:00 and 19:00.

# ### Which products are often sold together?

# In[31]:


# If the order ID is the same,then the products were ordered together

# https://stackoverflow.com/questions/43348194/pandas-select-rows-if-id-appear-several-time
df = all_data[all_data['Order ID'].duplicated(keep=False)]

# Referenced: https://stackoverflow.com/questions/27298178/concatenate-strings-from-several-rows-using-pandas-groupby
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df = df[['Order ID', 'Grouped']].drop_duplicates()

df.head()


# In[34]:


# Referenced: https://stackoverflow.com/questions/52195887/counting-unique-pairs-of-numbers-into-a-python-dictionary
from itertools import combinations
from collections import Counter

count = Counter()

for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))

for key,value in count.most_common(10):
    print(key, value)


# Interpreting the results:
# * iPhones and Lightning Charging Cables are frequently sold together (this combination appeared 1005 times)
# * Google Phones and USB-C Charging Cables are also frequently sold together (this combination appeared 987 times)

# ### Which products sold the most?

# In[36]:


product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

keys = [pair for pair, df in product_group]
plt.bar(keys, quantity_ordered)
plt.xticks(keys, rotation='vertical', size=8)
plt.ylabel('Quantity Ordered')
plt.xlabel('Product')
plt.show()


# Interpreting the results:
# * AAA Batteries (4-pack) were ordered the most while AA Batteries (4-pack) had the second highest quantity ordered.
# * The LG Dryer and Washing Machine had the lowest quantity ordered.

# ### Is there a correlation between a product's price and the quantity ordered?

# In[38]:


# Referenced: https://stackoverflow.com/questions/14762181/adding-a-y-axis-label-to-secondary-y-axis-in-matplotlib
prices = all_data.groupby('Product').mean()['Price Each']

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(keys, quantity_ordered, color='g')
ax2.plot(keys, prices, color='b')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color='g')
ax2.set_ylabel('Price ($)', color='b')
ax1.set_xticklabels(keys, rotation='vertical', size=8)

fig.show()


# Interpreting the results:
# * Cheaper items like batteries and lightning cables sold much more than more expensive items like a TV and dryer. 
# * Although laptops are more expensive than home appliances, the Macbook Pro Laptop and ThinkPad Laptop had a higher quantity ordered than the LG Dryer and Washing Machine. This may be because more people need a laptop than a dryer or washing machine.

# ## Conclusion

# 1. December had the highest number of sales and thus, earned the most. This is probably due to the holiday season.
# 2. San Francisco, CA had the highest number of sales.
# 3. Most of the orders are made around 11:00 and 19:00 so having advertisements around these times would be the most effective.
# 4. iPhones and charging cables as well as Google Phones and charging cables are frequently sold together. 
# 5. Cheaper items like AA and AAA batteries sold the most while more expensive items like a dryer and washing machine sold the least.

# In[ ]:




