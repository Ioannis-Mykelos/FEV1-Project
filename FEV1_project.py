#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('smoking.txt', sep=" ", delimiter = "\t", header=None)
data.columns = ["Age", "FEV1 (liters)", "Height (Inch)", "Gender", "Smoking Status", "Weight"]
print(data)

"""Forced Expiratory Volume in one second (FEV1), measures the volume that a person can exhale in the first second of a 
forceful expiration after a full inspiration.This measure will be used as an indicator of lung function in this
assignment."""


# In[2]:


# Exercise 2. Write a script which computes the average lung function, measured in FEV1, among the smokers and among the non-smokers,
# We will split the data set into two smaller data sets. One for smokers and one for non smokers.
# We will compute the average lung function, measured in FEV1, among the smokers and among the non-smokers.

smokers=data[data["Smoking Status"]==1]
non_smokers=data[data["Smoking Status"]==0]

mean_smokers_FEV1=smokers["FEV1 (liters)"].mean()
mean_non_smokers_FEV1=non_smokers["FEV1 (liters)"].mean()

print(mean_smokers_FEV1,mean_non_smokers_FEV1)


# In[3]:


# Exercise 2 (Boxplots). Make a box plot of the FEV1 in the two groups. What do you see?
# Are you surprised?

plt.boxplot([smokers["FEV1 (liters)"],non_smokers["FEV1 (liters)"]])
plt.xticks([1,2],['Smokers','Non-smokers'])
plt.ylabel('FEV1')
plt.title('Boxplox for smokers and non-smokers')
plt.show()


# In[4]:


# Find the unique values for each column

data_unique=data.nunique(axis=0)
print(data_unique)


# In[5]:


# Make a plot that relates the age with the mean FEV1
data=data.sort_values(by=["Age"], ascending=True)
mean_FEV1_per_age=[]
for i in data["Age"].unique():
    data_2=data[data["Age"]==i]
    mean_Fev1_perage=data_2["FEV1 (liters)"].mean()
    mean_FEV1_per_age.append(mean_Fev1_perage)
min_1=data["Age"].min()
max_2=data["Age"].max()
plt.plot(data["Age"].unique(),mean_FEV1_per_age,'o--',c="r")
plt.xlabel("Age")
plt.ylabel('Average FEV1')
plt.xlim(min_1-1, max_2+1)
plt.title('Age vs FEV1')
plt.show()


# In[6]:


#Exercise 3. Check the correlation (Pearson's r, Spearman's rho, Kendall's tau) between age and FEV1 
Age=data["Age"]
FEV1=data["FEV1 (liters)"]
print("The Pearson's r correlation is "+ str(Age.corr(FEV1)))
print("The Pearson's rho correlation is "+ str(Age.corr(FEV1, method='spearman')))
print("The Kendal's tau correlation is "+ str(Age.corr(FEV1, method='kendall') ))


# In[7]:


#First we will make a new table with first column the Age and second column FEV1
Age_FEV1 = pd.DataFrame({'Age': Age, 'FEV1': FEV1})
print(Age_FEV1.corr())
print(Age_FEV1.corr(method='spearman'))
print(Age_FEV1.corr(method='kendall'))


# In[8]:


# Pearson's r heatmap
corr=Age_FEV1.corr()
ax = plt.axes()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True)
ax.set_title('Pearsons r heatmap')
plt.show()


# Spearman's rho heatmap
corr1=Age_FEV1.corr(method='spearman')
ax = plt.axes()
sns.heatmap(corr1, xticklabels=corr1.columns, yticklabels=corr1.columns, annot=True)
ax.set_title('Spearman rho heatmap')
plt.show()


# # Kendall's tau heatmap
corr2=Age_FEV1.corr(method='kendall')
ax = plt.axes()
sns.heatmap(corr2, xticklabels=corr2.columns, yticklabels=corr2.columns, annot=True)
ax.set_title('Kendalls tau heatmap')
plt.show()


# In[9]:


#Exercise 5 (Histograms). Create a histogram over the age of subjects in each of the two groups smokers and non-smokers.
from matplotlib.pyplot import hist

plt.hist(smokers["Age"], bins=10,color='red')
plt.ylabel("# of students")
plt.xlabel("Age")
plt.xticks(data["Age"].unique())
plt.title('Histogram over the age of smokers')
plt.xlim(smokers["Age"].min()-1, smokers["Age"].max()+1)
plt.show()


# In[10]:


plt.hist(non_smokers["Age"], bins=10,color='blue')
plt.ylabel("# of students")
plt.xlabel("Age")
plt.xticks(data["Age"].unique())
plt.title('Histogram over the age of non smokers')
plt.xlim(non_smokers["Age"].min()-1, non_smokers["Age"].max()+1)
plt.show()


# In[ ]:




