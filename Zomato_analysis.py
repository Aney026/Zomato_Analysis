#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df =pd.read_csv('Zomato_data.csv')


# In[5]:


df.head()


# In[6]:


df


# Covert the data type of column - rate 

# In[7]:


def handleRate(value):
    value = str(value).split('/')
    value = value[0];
    return float(value)

df['rate'] = df['rate'].apply(handleRate)
df.head()


# In[8]:


df.info()


# Type of restaurant 

# In[9]:


df.head()


# In[10]:


sns.countplot(x=df['listed_in(type)'])
plt.xlabel ('Type of Restaurant')


# Conclusion - Majority of the restaurant fall in dining category

# In[14]:


group_data= df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': group_data})
plt.plot(result,c ="blue", marker = "o")
plt.xlabel("Type of Restaurant", c= "black",size=15)
plt.ylabel('Votes',c='black',size=15)


# Conclusion - Dininng restaurant has received max votes

# In[15]:


df.head()


# In[19]:


plt.hist(df['rate'],bins =10)
plt.title ('Ratings Distribution')
plt.show()


# Conclusion- the majority restaurant received rating from 3.3 to 4

# In[20]:


df.head()


# In[22]:


couple_data = df['approx_cost(for two people)']
sns.countplot(x=couple_data)


# Conclusion- the majority of couple prefer restaurant with an apporx cost of 300 rupees.

# In[23]:


plt.figure(figsize=(6,6))
sns.boxplot(x='online_order',y='rate',data = df)


# Conclusion- Online orders recieve higher rating in comparision to offline orders

# In[26]:


pivot_table = df.pivot_table(index='listed_in(type)',columns = 'online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivot_table, annot= True, cmap= 'YlGnBu',fmt='d')
plt.title("Heatmap")
plt.xlabel('Online Order')
plt.xlabel('Listed in(type)')
plt.show()


# Conclusion - Dining reataurants primarly accept offline orders, whereas cafes primarly receive online orders. This suggests that clients prefer orders in person at restaurants, but prefer online ordering at cafes.

# In[ ]:




