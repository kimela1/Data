#!/usr/bin/env python
# coding: utf-8

# 

# ### Import Hubway database

# In[1]:


import sqlite3
import pandas as pd
db = sqlite3.connect('hubway.db')
def run_query(query):
    return pd.read_sql_query(query,db)


# # Pull data from the trips table

# ### What was the duration of the longest trip?

# In[2]:


query = '''
SELECT duration FROM trips
ORDER BY duration DESC
LIMIT 1;
'''
run_query(query)


# #### Return the 10 highest trip durations

# In[3]:


query = '''
SELECT duration FROM trips
ORDER BY duration DESC
LIMIT 10;
'''
run_query(query)


# #### Return every column in trips where the duration was longer than 9990 seconds

# In[4]:


query = '''
SELECT * FROM trips
WHERE duration > 9990;
'''
run_query(query)


# #### Return trips with a duration longer than 9990 by 'registered' users

# In[5]:


query = '''
SELECT * FROM trips
WHERE (duration >= 9990) AND (sub_type = "Registered")
ORDER BY duration DESC;
'''
run_query(query)


# ### How many trips were taken by 'registered' users?

# In[6]:


query = '''
SELECT COUNT(*) AS "Total Trips by Registered Users"
FROM trips
WHERE sub_type = "Registered";
'''
run_query(query)


# ### What was the average trip duration?

# In[7]:


query = '''
SELECT AVG(duration) AS "Average Duration"
FROM trips;
'''
run_query(query)


# ### Do registered or casual users take longer trips?

# In[8]:


query = '''
SELECT sub_type, AVG(duration) AS "Average Duration"
FROM trips
GROUP BY sub_type;
'''
run_query(query)


# ### Which bike was used for the most trips?

# In[9]:


query = '''
SELECT bike_number as "Bike Number", COUNT(*) AS "Number of Trips"
FROM trips
GROUP BY bike_number
ORDER BY COUNT(*) DESC
LIMIT 1;
'''
run_query(query)


# ### What is the average duration of trips by users over the age of 30?

# In[10]:


query = '''
SELECT AVG(duration) FROM trips
WHERE (2017 - birth_date) > 30;
'''
run_query(query)


# # Include data from the stations table

# In[11]:


query = '''
SELECT * FROM stations
LIMIT 5;
'''
run_query(query)


# ### Which station is the most frequent starting point?

# In[12]:


query = '''
SELECT stations.station AS "Station", COUNT(*) AS "Count"
FROM trips INNER JOIN stations
ON trips.start_station = stations.id GROUP BY stations.station ORDER BY COUNT(*) DESC
LIMIT 5;
'''
run_query(query)


# ### Which stations are most frequently used for round trips?

# In[13]:


query = '''
SELECT stations.station AS "Station", COUNT(*) AS "Count"
FROM trips INNER JOIN stations
ON trips.start_station = stations.id
WHERE trips.start_station = trips.end_station
GROUP BY stations.station
ORDER BY COUNT(*) DESC
LIMIT 5;
'''
run_query(query)


# ### How many trips start and end in different municipalities?

# In[14]:


query = '''
SELECT COUNT(trips.id) AS "Count"
FROM trips INNER JOIN stations AS start
ON trips.start_station = start.id
INNER JOIN stations AS end
ON trips.end_station = end.id
WHERE start.municipality <> end.municipality;
'''
run_query(query)


# ### How many trips incurred additional fees (lasted longer than 30 minutes)?

# In[24]:


query = '''
SELECT COUNT(duration) AS "Count"
FROM trips
WHERE duration > 1800;
'''
run_query(query)


# ### Which bike was used for the longest total time?

# In[63]:


query = '''
SELECT bike_number as "Bike Number", COUNT(duration) as "Total Duration"
FROM trips
GROUP BY bike_number
ORDER BY COUNT(duration) DESC
LIMIT 5;
'''
run_query(query)


# ### Did registered or casual users take more round trips?

# In[62]:


query = '''
SELECT sub_type, COUNT(*) AS "Count"
FROM trips INNER JOIN stations
ON trips.start_station = stations.id
WHERE trips.start_station = trips.end_station
GROUP BY sub_type
'''
run_query(query)


# ### Which municipality had the longest average duration?

# In[76]:


query = '''
SELECT municipality, AVG(duration) avg_duration
FROM trips INNER JOIN stations
WHERE trips.start_station = stations.id
GROUP BY municipality
ORDER BY 2 DESC;
'''
run_query(query)


# In[ ]:




