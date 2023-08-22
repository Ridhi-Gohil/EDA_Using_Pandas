#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('display.max_columns', 200)


# In[7]:


plt.style.available


# In[8]:


df = pd.read_csv(r'\coaster_db.csv')
df


# In[10]:


df.shape


# In[12]:


df.head(5)


# In[13]:


df.columns


# In[14]:


df.dtypes


# In[16]:


df.describe()


# In[20]:


df = df[['coaster_name', #'Length', 'Speed', 
    'Location', 'Status', 
    #'Opening date','Type', 
    'Manufacturer', 
    #'Height restriction', 'Model', 'Height',
       #'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
      # 'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
       #'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
      # 'Track layout', 'Fastrack available', 'Soft opening date.1',
      # 'Closing date', 'Opened', 'Replaced by', 'Website',
      # 'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
      # 'Single rider line available', 'Restraint Style',
      # 'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced', 'latitude', 'longitude', 'Type_Main',
       'opening_date_clean', #'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph', #'height_value', 'height_unit', 
    'height_ft',
       'Inversions_clean', 'Gforce_clean']].copy()


# In[21]:


df.shape


# In[23]:


df.columns


# In[25]:


df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])


# In[27]:


df = df.rename(columns={'coaster_name':'Coaster_Name',
                   'year_introduced':'Year_Introduced',
                   'opening_date_clean':'Opening_Date',
                   'speed_mph':'Speed_mph',
                   'height_ft':'Height_ft',
                   'Inversions_clean':'Inversions',
                   'Gforce_clean':'Gforce'})


# In[32]:


df.isna().sum()


# In[36]:


df.duplicated()


# In[39]:


df.loc[df.duplicated(subset=['Coaster_Name'])].head(5)


# In[40]:


df.query('Coaster_Name == "Crystal Beach Cyclone"')


# In[51]:


df = df.loc[~df.duplicated(subset = ['Coaster_Name','Location','Opening_Date'])].reset_index(drop=True).copy()


# In[55]:


df['Year_Introduced'].value_counts()


# In[63]:


ax = df['Year_Introduced'].value_counts().head(10).plot(kind='bar', title='Top 10 Years Coasters Introduced')
ax.set_xlabel('Year Introduced')
ax.set_ylabel('Count')


# In[82]:


ax2 = df['Speed_mph'].plot(kind='hist', bins = 20, title ='Coaster Speed(mph)')
ax2.set_xlabel('Speed(mph)')
plt.show()           #removes the extra text written above the plot


# In[81]:


ax = df['Speed_mph'].plot(kind='kde', title='Coaster Speed (mph)')
ax.set_xlabel('Speed (mph)')
plt.show()


# In[80]:


df.plot(kind='scatter', x='Speed_mph', y='Height_ft',
       title='Coaster Speed vs Height')
plt.show()


# In[92]:


sns.scatterplot(x='Speed_mph', y='Height_ft',
               hue='Year_Introduced',
               data = df)
plt.show()


# In[94]:


sns.pairplot(data=df, vars=['Year_Introduced','Speed_mph',
                   'Height_ft','Inversions','Gforce'],
            hue='Type_Main')
plt.show()


# In[100]:


df_corr = df[['Year_Introduced','Speed_mph','Height_ft','Inversions','Gforce']].dropna().corr()


# In[103]:


sns.heatmap(df_corr, annot = True)
plt.show()


# In[125]:


#What are the locations with the fastest roller coasters (minimum of 10)?

ax = df.query('Location != "Other"').groupby('Location')['Speed_mph'].agg(['mean','count']).query('count >= 10')\
.sort_values('mean')['mean'].plot(kind='barh', figsize=(10, 5), title='Average Coaster Speed by Location')
ax.set_xlabel('Average Coaster Speed')
plt.show()


# In[ ]:





# In[ ]:




