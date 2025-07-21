#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pytrends


# In[2]:


import pandas as pd 
from pytrends.request import TrendReq 
import matplotlib.pyplot as plt 
Trending_topics = TrendReq(hl='en-US', tz=360)


# In[61]:


kw_list=["Instagram"] 
Trending_topics.build_payload(kw_list,cat=0, timeframe='today 12-m')


# In[63]:


from pytrends.request import TrendReq
import pandas as pd

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Build the payload
kw_list = ["Instagram"]
pytrends.build_payload(kw_list, cat=0, timeframe='2018-01-01 2018-02-01', geo='IN', gprop='')

# Get interest over time
data = pytrends.interest_over_time()

# Sort the data
data = data.sort_values(by="Instagram", ascending=False)

# Get the top 10 results
data = data.head(10)

# Print the results
print(data)


# In[68]:


# Function to get interest by region with retry mechanism
def get_interest_by_region_with_retry(pytrends, retries=3, delay=10):
    for i in range(retries):
        try:
            # Get interest by region
            data = pytrends.interest_by_region()
            return data
        except pytrends.exceptions.TooManyRequestsError:
            print(f"Rate limit exceeded. Retrying in {delay} seconds...")
            time.sleep(delay)
    raise Exception("Failed to retrieve data after multiple retries.")

# Get the data with retry logic
data = get_interest_by_region_with_retry(pytrends)

# Sort the data
data = data.sort_values(by="Instagram", ascending=False)

# Get the top 10 results
data = data.head(20)

print("Top 20 regions with highest interest in Instagram:")
print(data)


# In[69]:


data.reset_index().plot(x='geoName', y='Instagram', 
                        figsize=(10,5), kind="bar") 
plt.style.use('fivethirtyeight') 
plt.show()


# In[47]:


df = Trending_topics.top_charts(2020, hl='en-US', 
                                tz=300, geo='IN') 
df.head(10) 


# In[43]:


from pytrends.request import TrendReq

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25))

# Function to fetch and display related queries and interest by region
def get_data(kw):
    # Build payload and fetch interest by region
    pytrends.build_payload([kw], cat=0, timeframe='today 12-m', geo='IN', gprop='')
    interest_by_city_df = pytrends.interest_by_region(resolution='CITY')
    
    # Print related queries
    related_queries = pytrends.related_queries()[kw]['top'] if 'top' in pytrends.related_queries()[kw] else []
    print(f"Related queries for '{kw}':\n{related_queries}\n")
    
# Example usage
if __name__ == "__main__":
    keyword = 'Instagram'  # Replace with any keyword you want to analyze
    get_data(keyword)


# In[39]:


keywords = Trending_topics.suggestions( 
keyword='Data Science') 
df = pd.DataFrame(keywords) 
df.drop(columns= 'mid') 


# In[42]:


from pytrends.request import TrendReq

# Initialize Pytrends with a longer timeout
pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25))  # (connect timeout, read timeout)

# Build the payload
kw_list = ["Instagram"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='IN', gprop='')

# Try fetching the interest by region again
interest_by_city_df = pytrends.interest_by_region(resolution='PUNE')
print(interest_by_city_df.to_string())


# In[79]:


# Plotting the data
interest_by_city_df_sorted = interest_by_city_df.sort_values(by=kw_list[0], ascending=False)
top_10_cities = interest_by_city_df_sorted.head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_10_cities.index, top_10_cities[kw_list[0]], color='skyblue')
plt.xlabel('Interest Score')
plt.title(f'Top 10 Cities in India interested in "{kw_list[0]}"')
plt.gca().invert_yaxis()  # Invert y-axis to display highest interest at the top
plt.tight_layout()
plt.show()


# In[83]:



# Prepare data for pie chart
labels = top_10_cities.index
sizes = top_10_cities[kw_list[0]]
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # explode 1st slice

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title(f'Interest in "{kw_list[0]}" by Top 10 Cities in India\n')
plt.show()


# In[ ]:




