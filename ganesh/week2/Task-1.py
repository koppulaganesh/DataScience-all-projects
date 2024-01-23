#!/usr/bin/env python
# coding: utf-8

# # TASK-1

# In[39]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import datetime


# In[40]:


df=pd.read_csv(r"C:\Users\ganig\OneDrive\Desktop\Dataset\Manpower_SF_Nov12.csv")


# In[41]:


df.rename(columns={'plant_code': 'classes',
                   "absentee":"cost",
                   "total_attend_hours":"hours",
                   "jobtitle":"job",
                   "attend_type_code":"code"}, inplace=True)
df.drop(columns=["plan_cd","dept",
                 "division","direct_indirect",
                 "employee_class","workforce_category_descr",
                 "attend_reason_code","plant_line_running"],inplace=True)


# In[42]:


df


# Taking the 2 months data **(oct & nov)**

# In[43]:


start_date = '2023-10-01'
end_date = '2023-11-30'
df = df[(df['attend_date'] >= start_date) & (df['attend_date'] <= end_date)]


# In[44]:


df


# # Box Plot (without Groupby)

#  1. **Box Plot** between job vs cost

# In[45]:


fig = px.box(df, x='job', y="cost", template = 'plotly_dark',title='job vs cost',color="classes")
fig.update_layout(title=dict(text='Box Plot b/w job vs cost', font=dict(size=45,color="orange")))
fig.show()


# ![graph](Graph1.png)

# 2. **Box Plot** between job vs hours

# In[46]:


fig = px.box(df, x='job', y="hours", template = 'plotly_dark',title='job vs hours',color="code")
fig.update_layout(title=dict(text='Box Plot b/w job vs hours', font=dict(size=45,color="yellow")))
fig.show()


# ![graph](Graph2.png)

# # Plots With Groupby

# In[47]:


df1=df.groupby("attend_date")


# In[48]:


df1.head(2)


# # Line Plot

# 3. **Line Plot** between attend_date vs cost

# In[49]:


df2=df.groupby(['attend_date']).agg('sum').reset_index()
fig = px.line(df2, x='attend_date', y="cost", template = 'plotly_dark',title='attend_date vs cost')
fig.update_layout(title=dict(text='Line Plot b/w attend_date vs cost', font=dict(size=45,color="pink")))
fig.show()


# ![graph](Graph3.png)

# 4. **Line Plot** between attend_date vs hours

# In[50]:


df2=df.groupby(['attend_date']).agg('sum').reset_index()
fig = px.line(df2, x='attend_date', y="hours", template = 'plotly_dark',title='attend_date vs hours')
fig.update_layout(title=dict(text='Line Plot b/w attend_date vs hours', font=dict(size=45,color="Yellow")))
fig.show()


# ![graph](Graph4.png)

# # Bar Plot

# 5. **Bar Plot** between attend_date vs cost

# In[51]:


df2=df.groupby(['attend_date']).agg('sum').reset_index()
df2.sort_values('attend_date', inplace=True)
fig = px.bar(df2, x='attend_date', y="cost", template = 'plotly_dark',
             color="cost",text="attend_date",title='attend_date vs cost')
fig.update_layout(title=dict(text='Bar Plot b/w attend_date vs cost',font=dict(size=45, color="white")))
fig.show()


# ![graph](Graph5.png)

# 6. **Bar Plot** between attend_date vs hours

# In[52]:


df2=df.groupby(['attend_date']).agg('sum').reset_index()
df.sort_values('attend_date', inplace=True)
fig = px.bar(df2, x='attend_date',
             y="hours",template = 'plotly_dark',
             title='attend_date vs hours',color="hours",text="attend_date")
fig.update_layout(title=dict(text='Bar Plot b/w attend_date vs hours',font=dict(size=45, color="white")))
#fig.update_xaxes(categoryorder='total ascending')

import warnings
warnings.filterwarnings("ignore")   #to ignore warnings

fig.show()


# ![graph](Graph6.png)

# # Scatter Plot

# 7. **Scatter Plot** between cost vs hours

# In[53]:


df2=df.groupby(["attend_date"]).agg('sum').reset_index()
fig = px.scatter(df2, x='cost', y="hours", template = 'plotly_dark',title='cost vs hours')
fig.update_layout(title=dict(text='Scatter Plot b/w cost vs hours', font=dict(size=45, color="red")))
fig.show()


# ![graph](Graph7.png)

# In[ ]:




