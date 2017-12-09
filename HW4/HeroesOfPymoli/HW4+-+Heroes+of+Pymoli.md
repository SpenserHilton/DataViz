

```python
#Import dependencies
import pandas as pd
import numpy as np
```


```python
#Establish original dataframe
original_df = pd.read_json("purchase_data.json")
original_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Find total number of players. Some occur repeatedly. Filtering out duplicate players
totalplayers = len(original_df["SN"].value_counts())
totalplayer_df = pd.DataFrame([{"Total Players": totalplayers}])
totalplayer_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>2.931192</td>
      <td>780</td>
      <td>2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.151832</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.452007</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other</th>
      <td>1.396161</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>2.950521</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>2.815515</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Other/Non-Disclosed</th>
      <td>11</td>
      <td>3.249091</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>34-38</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>18-22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>18-22</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>22-26</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20</td>
      <td>Male</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Tanimnya91</td>
      <td>18-22</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>Male</td>
      <td>153</td>
      <td>Mercenary Sabre</td>
      <td>4.57</td>
      <td>Undjaskla97</td>
      <td>18-22</td>
    </tr>
    <tr>
      <th>7</th>
      <td>29</td>
      <td>Female</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Iathenudil29</td>
      <td>26-30</td>
    </tr>
    <tr>
      <th>8</th>
      <td>25</td>
      <td>Male</td>
      <td>118</td>
      <td>Ghost Reaver, Longsword of Magic</td>
      <td>2.77</td>
      <td>Sondenasta63</td>
      <td>22-26</td>
    </tr>
    <tr>
      <th>9</th>
      <td>31</td>
      <td>Male</td>
      <td>99</td>
      <td>Expiration, Warscythe Of Lost Worlds</td>
      <td>4.53</td>
      <td>Hilaerin92</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>10</th>
      <td>24</td>
      <td>Male</td>
      <td>57</td>
      <td>Despair, Favor of Due Diligence</td>
      <td>3.81</td>
      <td>Chamosia29</td>
      <td>22-26</td>
    </tr>
    <tr>
      <th>11</th>
      <td>20</td>
      <td>Male</td>
      <td>47</td>
      <td>Alpha, Reach of Ending Hope</td>
      <td>1.55</td>
      <td>Sally64</td>
      <td>18-22</td>
    </tr>
    <tr>
      <th>12</th>
      <td>30</td>
      <td>Male</td>
      <td>81</td>
      <td>Dreamkiss</td>
      <td>4.06</td>
      <td>Iskossa88</td>
      <td>26-30</td>
    </tr>
    <tr>
      <th>13</th>
      <td>23</td>
      <td>Male</td>
      <td>77</td>
      <td>Piety, Guardian of Riddles</td>
      <td>3.68</td>
      <td>Seorithstilis90</td>
      <td>22-26</td>
    </tr>
    <tr>
      <th>14</th>
      <td>40</td>
      <td>Male</td>
      <td>44</td>
      <td>Bonecarvin Battle Axe</td>
      <td>2.46</td>
      <td>Sundast29</td>
      <td>38-42</td>
    </tr>
    <tr>
      <th>18</th>
      <td>28</td>
      <td>Male</td>
      <td>91</td>
      <td>Celeste</td>
      <td>3.71</td>
      <td>Iskista88</td>
      <td>26-30</td>
    </tr>
    <tr>
      <th>19</th>
      <td>31</td>
      <td>Male</td>
      <td>177</td>
      <td>Winterthorn, Defender of Shifting Worlds</td>
      <td>4.89</td>
      <td>Assossa43</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>20</th>
      <td>24</td>
      <td>Male</td>
      <td>78</td>
      <td>Glimmer, Ender of the Moon</td>
      <td>2.33</td>
      <td>Irith83</td>
      <td>22-26</td>
    </tr>
    <tr>
      <th>21</th>
      <td>15</td>
      <td>Male</td>
      <td>3</td>
      <td>Phantomlight</td>
      <td>1.79</td>
      <td>Iaralrgue74</td>
      <td>14-18</td>
    </tr>
    <tr>
      <th>22</th>
      <td>11</td>
      <td>Female</td>
      <td>11</td>
      <td>Brimstone</td>
      <td>2.52</td>
      <td>Deural48</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>24</th>
      <td>11</td>
      <td>Male</td>
      <td>65</td>
      <td>Conqueror Adamantite Mace</td>
      <td>1.96</td>
      <td>Qarwen67</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>26</th>
      <td>29</td>
      <td>Male</td>
      <td>132</td>
      <td>Persuasion</td>
      <td>3.90</td>
      <td>Aerithllora36</td>
      <td>26-30</td>
    </tr>
    <tr>
      <th>27</th>
      <td>34</td>
      <td>Male</td>
      <td>106</td>
      <td>Crying Steel Sickle</td>
      <td>2.29</td>
      <td>Assastnya25</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>28</th>
      <td>15</td>
      <td>Male</td>
      <td>49</td>
      <td>The Oculus, Token of Lost Worlds</td>
      <td>4.23</td>
      <td>Ilariarin45</td>
      <td>14-18</td>
    </tr>
    <tr>
      <th>29</th>
      <td>16</td>
      <td>Female</td>
      <td>45</td>
      <td>Glinting Glass Edge</td>
      <td>2.46</td>
      <td>Phaedai25</td>
      <td>14-18</td>
    </tr>
    <tr>
      <th>31</th>
      <td>18</td>
      <td>Male</td>
      <td>37</td>
      <td>Shadow Strike, Glory of Ending Hope</td>
      <td>1.93</td>
      <td>Iarilis73</td>
      <td>14-18</td>
    </tr>
    <tr>
      <th>37</th>
      <td>31</td>
      <td>Male</td>
      <td>171</td>
      <td>Scalpel</td>
      <td>3.62</td>
      <td>Sondossa91</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>46</th>
      <td>11</td>
      <td>Male</td>
      <td>17</td>
      <td>Lazarus, Terror of the Earth</td>
      <td>3.47</td>
      <td>Palatyon26</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>51</th>
      <td>16</td>
      <td>Male</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Reula64</td>
      <td>14-18</td>
    </tr>
    <tr>
      <th>68</th>
      <td>11</td>
      <td>Male</td>
      <td>38</td>
      <td>The Void, Vengeance of Dark Magic</td>
      <td>2.82</td>
      <td>Qarwen67</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>70</th>
      <td>7</td>
      <td>Female</td>
      <td>158</td>
      <td>Darkheart, Butcher of the Champion</td>
      <td>3.56</td>
      <td>Eosurdru76</td>
      <td>0-10</td>
    </tr>
    <tr>
      <th>79</th>
      <td>29</td>
      <td>Male</td>
      <td>144</td>
      <td>Blood Infused Guardian</td>
      <td>2.86</td>
      <td>Undirrala66</td>
      <td>26-30</td>
    </tr>
    <tr>
      <th>81</th>
      <td>38</td>
      <td>Male</td>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>Yaristi64</td>
      <td>34-38</td>
    </tr>
    <tr>
      <th>106</th>
      <td>37</td>
      <td>Female</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Chadossa56</td>
      <td>34-38</td>
    </tr>
    <tr>
      <th>117</th>
      <td>11</td>
      <td>Male</td>
      <td>160</td>
      <td>Azurewrath</td>
      <td>2.22</td>
      <td>Qarwen67</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>121</th>
      <td>7</td>
      <td>Male</td>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>Lassjask63</td>
      <td>0-10</td>
    </tr>
    <tr>
      <th>125</th>
      <td>7</td>
      <td>Female</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Heosurnuru52</td>
      <td>0-10</td>
    </tr>
    <tr>
      <th>170</th>
      <td>9</td>
      <td>Male</td>
      <td>71</td>
      <td>Demise</td>
      <td>4.07</td>
      <td>Reulae52</td>
      <td>0-10</td>
    </tr>
    <tr>
      <th>175</th>
      <td>35</td>
      <td>Male</td>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>4.14</td>
      <td>Raillydeu47</td>
      <td>34-38</td>
    </tr>
    <tr>
      <th>179</th>
      <td>40</td>
      <td>Male</td>
      <td>70</td>
      <td>Hope's End</td>
      <td>3.89</td>
      <td>Chanosiaya39</td>
      <td>38-42</td>
    </tr>
    <tr>
      <th>186</th>
      <td>40</td>
      <td>Male</td>
      <td>144</td>
      <td>Blood Infused Guardian</td>
      <td>2.86</td>
      <td>Chanosiaya39</td>
      <td>38-42</td>
    </tr>
    <tr>
      <th>189</th>
      <td>35</td>
      <td>Male</td>
      <td>179</td>
      <td>Wolf, Promise of the Moonwalker</td>
      <td>1.88</td>
      <td>Raillydeu47</td>
      <td>34-38</td>
    </tr>
    <tr>
      <th>212</th>
      <td>40</td>
      <td>Male</td>
      <td>111</td>
      <td>Misery's End</td>
      <td>2.91</td>
      <td>Yarmol79</td>
      <td>38-42</td>
    </tr>
    <tr>
      <th>237</th>
      <td>7</td>
      <td>Male</td>
      <td>121</td>
      <td>Massacre</td>
      <td>3.42</td>
      <td>Lisistaya47</td>
      <td>0-10</td>
    </tr>
    <tr>
      <th>238</th>
      <td>40</td>
      <td>Female</td>
      <td>49</td>
      <td>The Oculus, Token of Lost Worlds</td>
      <td>4.23</td>
      <td>Chamadar27</td>
      <td>38-42</td>
    </tr>
    <tr>
      <th>264</th>
      <td>45</td>
      <td>Male</td>
      <td>124</td>
      <td>Venom Claymore</td>
      <td>2.72</td>
      <td>Marassaya49</td>
      <td>42-46</td>
    </tr>
    <tr>
      <th>644</th>
      <td>43</td>
      <td>Male</td>
      <td>57</td>
      <td>Despair, Favor of Due Diligence</td>
      <td>3.81</td>
      <td>Raesurdil91</td>
      <td>42-46</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age Group</th>
      <th>Total Purchases</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0-10</td>
      <td>32</td>
      <td>3.02</td>
      <td>96.62</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10-14</td>
      <td>31</td>
      <td>2.70</td>
      <td>83.79</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14-18</td>
      <td>111</td>
      <td>2.88</td>
      <td>319.32</td>
    </tr>
    <tr>
      <th>3</th>
      <td>18-22</td>
      <td>231</td>
      <td>2.93</td>
      <td>676.20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22-26</td>
      <td>207</td>
      <td>2.94</td>
      <td>608.02</td>
    </tr>
    <tr>
      <th>5</th>
      <td>26-30</td>
      <td>63</td>
      <td>2.98</td>
      <td>187.99</td>
    </tr>
    <tr>
      <th>6</th>
      <td>30-34</td>
      <td>46</td>
      <td>3.07</td>
      <td>141.24</td>
    </tr>
    <tr>
      <th>7</th>
      <td>34-38</td>
      <td>37</td>
      <td>2.81</td>
      <td>104.06</td>
    </tr>
    <tr>
      <th>8</th>
      <td>38-42</td>
      <td>20</td>
      <td>3.13</td>
      <td>62.56</td>
    </tr>
    <tr>
      <th>9</th>
      <td>42-46</td>
      <td>2</td>
      <td>3.26</td>
      <td>6.53</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>84</td>
      <td>Final Critic</td>
      <td>2.46</td>
      <td>11</td>
      <td>27.06</td>
    </tr>
    <tr>
      <th>1</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>1.03</td>
      <td>11</td>
      <td>11.33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>31</td>
      <td>Arcane Gem</td>
      <td>1.36</td>
      <td>9</td>
      <td>12.24</td>
    </tr>
    <tr>
      <th>3</th>
      <td>34</td>
      <td>Stormcaller</td>
      <td>2.23</td>
      <td>9</td>
      <td>20.07</td>
    </tr>
    <tr>
      <th>4</th>
      <td>175</td>
      <td>Serenity</td>
      <td>1.88</td>
      <td>9</td>
      <td>16.92</td>
    </tr>
  </tbody>
</table>
</div>




```python
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

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>84</td>
      <td>Final Critic</td>
      <td>2.46</td>
      <td>11</td>
      <td>27.06</td>
    </tr>
    <tr>
      <th>45</th>
      <td>34</td>
      <td>Stormcaller</td>
      <td>2.23</td>
      <td>9</td>
      <td>20.07</td>
    </tr>
    <tr>
      <th>46</th>
      <td>175</td>
      <td>Serenity</td>
      <td>1.88</td>
      <td>9</td>
      <td>16.92</td>
    </tr>
    <tr>
      <th>33</th>
      <td>31</td>
      <td>Arcane Gem</td>
      <td>1.36</td>
      <td>9</td>
      <td>12.24</td>
    </tr>
    <tr>
      <th>24</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>1.03</td>
      <td>11</td>
      <td>11.33</td>
    </tr>
  </tbody>
</table>
</div>


