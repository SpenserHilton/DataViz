
# coding: utf-8

# In[1]:


# Import the Pandas library
import pandas as pd


# In[2]:


# Create a reference the CSV file desired
csv_path = "../Resources/ufoSightings.csv"

# Read the CSV into a Pandas DataFrame
ufo_df = pd.read_csv(csv_path)

# Print the first five rows of data to the screen
ufo_df.head()


# In[3]:


# Check to see if there are any rows with missing data
ufo_df.count()


# In[4]:


# Remove the rows with missing data
clean_ufo_df = ufo_df.dropna(how="any")
clean_ufo_df.count()


# In[5]:


# Filter the data so that only those sightings in the US are in a DataFrame
usa_ufo_df = clean_ufo_df.loc[clean_ufo_df["country"] == "us",:]
usa_ufo_df


# In[6]:


# Count how many sightings have occured within each state
state_counts = usa_ufo_df["state"].value_counts()
state_counts


# In[7]:


# Convert the state_counts Series into a DataFrame
state_ufo_counts_df = pd.DataFrame(state_counts)
state_ufo_counts_df.head()


# In[8]:


# Convert the column name into "Sum of Sightings"
state_ufo_counts_df = state_ufo_counts_df.rename(columns={"state":"Sum of Sightings"})
state_ufo_counts_df.head()


# In[9]:


# Want to add up the seconds UFOs are seen? There is a problem
# Problem can be seen by examining datatypes within the DataFrame
usa_ufo_df.dtypes


# In[12]:


# Using to_numeric() to convert a column's data into floats
usa_ufo_df["duration (seconds)"] = pd.to_numeric(usa_ufo_df["duration (seconds)"])
usa_ufo_df.dtypes


# In[37]:


# Now it is possible to find the sum of seconds
usa_ufo_df["duration (seconds)"].sum()

