#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


df=pd.read_csv('d:\\t20.csv',encoding='latin-1')
df.head()


# In[9]:


df.describe()


# In[10]:


df.info()


# In[15]:


df.head()


# In[30]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x="Inns",y="Mat",data=df)


# In[31]:


df.corr()


# In[32]:


sns.heatmap(df.corr())


# In[36]:


Mat_name=df.Mat.value_counts().index
Runs_val=df.Runs.value_counts().values


# In[37]:


plt.pie(Mat_name[:3],labels=Runs_val[:3],autopct='%1.2f%%')


# In[40]:


df.isnull().sum()


# In[41]:


df.columns


# In[42]:


df


# In[52]:


sns.countplot(x="0",data=df,palette=['blue','red','orange','yellow','green','green'])


# In[63]:


df[df['Player']=='White'].groupby('Runs').size().reset_index()


# In[61]:


df.groupby(['Player','Runs']).size().reset_index().head(5)


# In[65]:


df[['Runs','Inns']].groupby(['Runs','Inns']).size().reset_index()


# In[76]:


sns.pairplot(df)


# In[77]:


df.Player.value_counts().index


# In[78]:


sns.distplot(df['Mat'])


# In[79]:


sns.distplot(df['Mat'],kde=False,bins=10)


# In[81]:


sns.countplot('Inns',data=df)


# In[90]:


sns.boxplot(x="Mat", y="Inns", data=df,palette='rainbow')


# In[89]:


sns.violinplot(x="Mat", y="Inns", data=df,palette='rainbow')

