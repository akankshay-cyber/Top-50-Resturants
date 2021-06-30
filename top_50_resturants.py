#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import seaborn as sns
import squarify
from wordcloud import WordCloud


# In[3]:


data=pd.read_csv('data_resturants.csv',encoding="utf-8")


# In[4]:


data.head(10)


# In[5]:


data.info()


# In[6]:


plt.figure(figsize=(10,5))
sns.heatmap(data.isnull(),cmap="magma",yticklabels=False,cbar=False)
plt.show()


# In[7]:


data["city"].unique()


# In[8]:


data[data["rating"].isnull()]


# In[9]:


data['rating'].unique()


# In[10]:


data.shape


# In[11]:


data.isnull().sum()


# In[12]:


data.shape


# In[13]:


data["rating"]= data["rating"].apply(lambda x:(str(x).replace(",","")))


# In[14]:


data = data[data['rating']!='others']
data['rating']=pd.to_numeric(data['rating'],errors='coerce')


# In[15]:


data['city'].unique()


# In[16]:


topfiftyresturants =[]
for resturants in data['name'].unique():
    df = data[data['name']==resturants]
    sum=np.sum(df['rating'])
    topfiftyresturants.append([resturants,sum])
resturants = pd.DataFrame(topfiftyresturants,columns=['Resturants Name','Resturants Rating'])
resturants.sort_values(by='Resturants Name',ascending=False,inplace=True)


# In[17]:


resturants


# In[18]:


data.shape


# In[19]:


resturants = resturants[:40]


# In[21]:


plt.figure(figsize=(20,50))
ax = sns.barplot(x = "Resturants Rating",y = "Resturants Name",data= resturants,palette = "husl",linewidth = 2,label = "big")
for i,j in enumerate(resturants["Resturants Rating"]):
    ax.text(10,i,j,weight="bold",color = 'black',fontsize=15,ha ='left')
plt.title("50 Top Resturants  with best Ratings", fontsize = 20)
ax.set_xlabel(xlabel = "Resturants Rating", fontsize = 20)
ax.set_ylabel(ylabel = "Resturants Name", fontsize = 20)
plt.show()
del resturants


# In[32]:


d = data[data['city']!='others']['city'].value_counts().head(6)
explode = (0.1,0,0,0,0,0)
fig1,ax1=plt.subplots(figsize=(20,10))
ax1.pie(d.values,explode=explode,labels=d.index,autopct ='%1.1f%%',shadow=True,startangle=140)
ax1.axis('equal')
plt.title("Top cities",fontsize=30)
plt.show()


# In[33]:


## From the above pie chart we can conclude that the most of the top universities are in :Jacksonville ,columbus, and valdosta.


# In[34]:


plt.figure(figsize=(17,12))
mean_amount = data.groupby('city').sum()['rating'].sort_values(ascending=False).head(15)
squarify.plot(sizes=mean_amount.values,label=mean_amount.index,value=mean_amount.values)
plt.title("Distribution of resturants according to ratings across different cities")


# In[35]:


##Jacksonville is the most preferred city for top notch resturants


# In[36]:


corr = data.corr()
ax = sns.heatmap(corr,
                vmin=-1,vmax=1,center=0,
                 cmap=sns.diverging_palette(20,220,n=200),
                 square = True
                )


# In[ ]:




