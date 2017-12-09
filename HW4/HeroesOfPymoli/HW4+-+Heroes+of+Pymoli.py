
# coding: utf-8

# In[127]:

#Import dependencies
import pandas as pd
import numpy as np


# In[128]:

#Establish original dataframe
original_df = pd.read_json("purchase_data.json")
original_df.head()


# In[129]:

#Find total number of players. Some occur repeatedly. Filtering out duplicate players
totalplayers = len(original_df["SN"].value_counts())
totalplayer_df = pd.DataFrame([{"Total Players": totalplayers}])
totalplayer_df.head()


# In[130]:

#PURCHASING ANALYSIS (TOTAL)
# Number of unique items
unique_items = len(original_df["Item Name"].value_counts())

#Average Purchase Price
mean_price = original_df["Price"].mean()

#Total Number of Purchases
total_purch = len(original_df)

#Total Revenue
pricelist = original_df["Price"].tolist()
totalrev= sum(pricelist)

purch_analysis_df = pd.DataFrame({"Number of Unique Items":[unique_items],
                                 "Average Price": [mean_price],
                                  "Number of Purchases": [total_purch],
                                  "Total Revenue": [totalrev]})
purch_analysis_df = purch_analysis_df[["Number of Unique Items", "Average Price", "Number of Purchases", "Total Revenue"]]
purch_analysis_df.head()


# In[131]:

#GENDER DEMOGRAPHICS

#Total players = 573
#Remove duplicate players
gender_df = original_df.drop_duplicates(["SN"])
#Males
total_male = gender_df.loc[gender_df.Gender == 'Male', 'Gender'].count()
male_perc = total_male/totalplayers*100
#Females
total_female = gender_df.loc[gender_df.Gender == 'Female', 'Gender'].count()
female_perc = total_female/totalplayers*100
#Other
total_other = totalplayers - total_male - total_female
other_perc = total_other/totalplayers*100

gen_demo_df = pd.DataFrame({"Percentage of Players": [male_perc, female_perc, other_perc],
                           "Total Count":[total_male, total_female, total_other]},index=["Male","Female","Other"])

gen_demo_df.head()


# In[132]:

#PURCHASING ANALYSIS (GENDER)
#separate dataframes by gender
male_df = original_df.loc[original_df["Gender"] == 'Male',:]
female_df = original_df.loc[original_df["Gender"]=='Female',:]
other_df = original_df.loc[original_df["Gender"] != "Male",:]
other_df = other_df.loc[other_df["Gender"]!= "Female",:]
#Purchase count, avg purch val, total purch val, normalized totals
    #Male
male_purch_count = len(male_df)
male_avg_val = male_df["Price"].mean()
male_tot_val = male_df["Price"].sum()
    #Female
female_purch_count = len(female_df)
female_avg_val = female_df["Price"].mean()
female_tot_val = female_df['Price'].sum()
    #Other
other_purch_count = len(other_df)
other_avg_val = other_df["Price"].mean()
other_tot_val = other_df["Price"].sum()

gender_purch_df = pd.DataFrame({"Purchase Count":[male_purch_count, female_purch_count, other_purch_count],
                               'Average Purchase Price': [male_avg_val, female_avg_val, other_avg_val],
                               'Total Purchase Value': [male_tot_val, female_tot_val, other_tot_val]}, index=['Male','Female','Other/Non-Disclosed'])
gender_purch_df = gender_purch_df[['Purchase Count', 'Average Purchase Price', 'Total Purchase Value']]
gender_purch_df.head()


# In[133]:

#AGE DEMOGRAPHICS
#bins
bins = [0,10,14,18,22,26,30,34,38,42,46]
#bin names
bin_names = ['0-10','10-14','14-18','18-22','22-26','26-30',
             '30-34','34-38','38-42','42-46']
#cut into bins
age_df = original_df

age_df["Age Group"] = pd.cut(original_df['Age'],bins, labels = bin_names)
#group by bins
age_groups= age_df.groupby(["Age Group"])
age_groups.head()


# In[134]:

#age demos df established. Get values
#new df's by bin
bin_0_10_df =age_df.loc[age_df['Age Group']=='0-10']
bin_10_14_df = age_df.loc[age_df['Age Group']=='10-14']
bin_14_18_df = age_df.loc[age_df['Age Group']=='14-18']
bin_18_22_df = age_df.loc[age_df['Age Group']=='18-22']
bin_22_26_df = age_df.loc[age_df['Age Group']=='22-26']
bin_26_30_df = age_df.loc[age_df['Age Group']=='26-30']
bin_30_34_df = age_df.loc[age_df['Age Group']=='30-34']
bin_34_38_df = age_df.loc[age_df['Age Group']=='34-38']
bin_38_42_df = age_df.loc[age_df['Age Group']=='38-42']
bin_42_46_df = age_df.loc[age_df['Age Group']=='42-46']
bin_df_list = [bin_0_10_df, bin_10_14_df, bin_14_18_df, bin_18_22_df, bin_22_26_df,
              bin_26_30_df, bin_30_34_df, bin_34_38_df, bin_38_42_df, bin_42_46_df]
bin_df_names = ['0-10','10-14','14-18','18-22','22-26',
                '26-30','30-34','34-38','38-42','42-46']

#calculations
purc_count_list = []
avg_purc_list =[]
total_purc_list = []
for df in bin_df_list:
    purc_count = len(df)
    purc_count_list.append(purc_count)
    avg_purc_price = df['Price'].mean()
    avg_purc_list.append(avg_purc_price)
    total_purc_val = df['Price'].sum()
    total_purc_list.append(total_purc_val)

#new df by bin
age_breakdown_df = pd.DataFrame(list(zip(bin_df_names, purc_count_list, 
                      avg_purc_list, total_purc_list)),
              columns=['Age Group','Total Purchases','Average Purchase Price',
                       'Total Purchase Value'])
age_breakdown_df.round(decimals=2)


# In[135]:

#MOST POPULAR ITEMS
''' Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value
'''
pop_id_list = original_df['Item ID'].value_counts().index.tolist()
pop_name_list = original_df['Item Name'].value_counts().index.tolist()
pop_count_list = original_df['Item ID'].value_counts().tolist()
pop_price_list = original_df['Price'].value_counts().index.tolist()

popular_df = pd.DataFrame({"Item ID": [pop_id_list[0],pop_id_list[1],pop_id_list[2],pop_id_list[3],pop_id_list[4]],
                          "Item Name":[pop_name_list[0],pop_name_list[1],pop_name_list[2],pop_name_list[3],pop_name_list[4]],
                          "Purchase Count":[pop_count_list[0],pop_count_list[1],pop_count_list[2],pop_count_list[3],pop_count_list[4]],
                          "Item Price":[pop_price_list[0],pop_price_list[1],pop_price_list[2],pop_price_list[3],pop_price_list[4]],
                         })
popular_df["Total Purchase Value"]= popular_df['Item Price'] * popular_df['Purchase Count']
    
popular_df.head()


# In[136]:

#MOST PROFITABLE ITEMS
'''Identify the 5 most profitable items by total purchase value, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value'''

profit_df = original_df.sort_values("Price", ascending=False)
sorted_profit_df = pd.merge(popular_df, profit_df, on="Item Name")
sorted_profit_df.drop(["Gender", "Item ID_y", "Price", 'SN', 'Age Group', "Age"], axis=1, inplace=True)
sorted_profit_df.rename(columns={'Item ID_x': 'Item ID'}, inplace=True)
sorted_profit_df = sorted_profit_df.sort_values('Total Purchase Value', ascending=False)
sorted_profit_df.drop_duplicates(['Item ID'], inplace=True)
sorted_proft_df=sorted_profit_df[["Item ID", "Item Name", "Purchase Count", "Item Price", "Total Purchase Value"]]
sorted_profit_df.head()

