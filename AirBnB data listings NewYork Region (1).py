#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn


# In[2]:


listings = pd.read_csv('listings.csv')


# In[3]:


listings


# In[4]:


sn.countplot(x = 'neighbourhood_group', data = listings)
plt.show


# In[5]:


sn.barplot(x = 'neighbourhood_group', y = 'price', data = listings)
plt.show()


# In[6]:


sn.barplot(x = 'neighbourhood_group', y = 'price', data = listings, ci = False)
plt.show()


# In[ ]:




