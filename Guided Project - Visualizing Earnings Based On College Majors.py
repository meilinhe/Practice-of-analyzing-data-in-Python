
# coding: utf-8

# In[30]:

import pandas as pd

#Read the dataset into a DataFrame and start exploring the data
recent_grads = pd.read_csv('recent-grads.csv')
first_row = recent_grads.iloc[1]
head = recent_grads.head()
tail = recent_grads.tail()
summary = recent_grads.describe()
print(first_row, head, tail, summary)

#Drop rows with missing values
raw_data_count = recent_grads.shape[0]
recent_grads = recent_grads.dropna()
cleaned_data_count = recent_grads.shape[0]
print(raw_data_count, cleaned_data_count)


# In[4]:

get_ipython().magic('matplotlib inline')

#Do students in more popular majors make more money? - No
ax1 = recent_grads.plot(x='Sample_size', y='Median', kind='scatter')
ax1.set_title('Median vs. Sample_size')

ax2 = recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')
ax2.set_title('Unemployment_rate vs. Sample_size')

#Is there any link between the number of full-time employees and median salary? - No
ax3 = recent_grads.plot(x='Full_time', y='Median', kind='scatter')
ax3.set_title('Median vs. Full_time')

ax4 = recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')
ax4.set_title('Unemployment_rate vs. ShareWomen')

ax5 = recent_grads.plot(x='Men', y='Median', kind='scatter')
ax5.set_title('Median vs. Men')

#Do students that majored in subjects that were majority female make more money? - No
ax6 = recent_grads.plot(x='Women', y='Median', kind='scatter')
ax6.set_title('Median vs. Women')


# In[35]:

import matplotlib.pyplot as plt 
fig = plt.figure(figsize = (10, 20))
ax1 = fig.add_subplot(4,2,1)
ax2 = fig.add_subplot(4,2,2)
ax3 = fig.add_subplot(4,2,3)
ax4 = fig.add_subplot(4,2,4)
ax5 = fig.add_subplot(4,2,5)
ax6 = fig.add_subplot(4,2,6)
ax7 = fig.add_subplot(4,2,7)
ax8 = fig.add_subplot(4,2,8)

ax1.hist(recent_grads['Sample_size'], bins = 20, range = (0, 5000))
ax2.hist(recent_grads['Median'], bins = 20, range = (0, 100000))
ax3.hist(recent_grads['Employed'], bins = 20, range = (0, 500000))
ax4.hist(recent_grads['Full_time'], bins = 20, range = (0, 500000))
ax5.hist(recent_grads['ShareWomen'], bins = 20, range = (0, 1))
ax6.hist(recent_grads['Unemployment_rate'], bins = 20, range = (0, 0.2))
ax7.hist(recent_grads['Men'], bins = 20, range = (0, 200000))
ax8.hist(recent_grads['Women'], bins = 20, range = (0, 500000))

#What percent of majors are predominantly male? Predominantly female? -
#What's the most common median salary range? - 30000 ~ 35000


# In[40]:

from pandas.tools.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize=(10,10))
scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize = (10, 10))


# In[57]:

recent_grads[:10].plot.bar(x='Major', y='ShareWomen')
recent_grads.tail(10).plot.bar(x='Major', y='ShareWomen')

recent_grads[:10].plot.bar(x='Major', y='Unemployment_rate')
recent_grads.tail(10).plot.bar(x='Major', y='Unemployment_rate')


# In[ ]:



