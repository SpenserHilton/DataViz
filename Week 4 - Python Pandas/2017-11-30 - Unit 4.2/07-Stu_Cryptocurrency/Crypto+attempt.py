
# coding: utf-8

# In[3]:

import pandas as pd
import csv
btc = "bitcoin_cash_price.csv"
dash = "dash_price.csv"


# In[8]:

#inital dataframes
btc_df = pd.read_csv(btc)
dash_df = pd.read_csv(dash)


# In[10]:

btc_df.head()


# In[13]:

dash_df.head()


# In[16]:

merged_df = pd.merge(btc_df, dash_df, on="Date")
merged_df.head()


# In[19]:

cleanmerge_df = merged_df.rename(columns={"Open_x":"BTC Open", "High_x":"BTC High", "Low_x":"BTC Low", "Close_x":"BTC Close", "Volume_x":"BTC Volume", "Market Cap_x":"BTC Market Cap", "Open_y":"Dash Open", "High_y":"Dash High", "Low_y":"Dash Low", "Close_y":"Dash Close", "Volume_y":"Dash Volume", "Market Cap_y":"Dash Market Cap"})
cleanmerge_df.head()


# In[ ]:



