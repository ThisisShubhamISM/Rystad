import pandas as pd

#read the time series for “US Refinery and Blender Net Input of Crude Oil” by PADD
df = pd.read_excel('test.xls')

#Keep data from January 2016 onwards, delete all other rows

df = df.iloc[660:, :]

df['Dates'] = pd.to_datetime(df['Date']).dt.date
df['Time'] = pd.to_datetime(df['Date']).dt.time

df["Year"] = df['Dates'].map(lambda x: x.year)
df["Quarter"] = df['Dates'].map(lambda x: x.month)
df["Month"] = df['Dates'].map(lambda x: x.month)


for i in range(df.shape[0]):
    if df.iloc[i,20] <=3:
        df.iloc[i,20] = 1
    
    elif df.iloc[i,20] <=6:
        df.iloc[i,20] = 2
        
    elif df.iloc[i,20] <=9:
        df.iloc[i,20] = 3
        
    elif df.iloc[i,20] <=12:
        df.iloc[i,20] = 4



df['(PADD 1) Refinery and Blender Net Input of Crude Oil'] = df.iloc[:,2]
df['(PADD 2) Refinery and Blender Net Input of Crude Oil'] = df.iloc[:,5]
df['(PADD 3) Refinery and Blender Net Input of Crude Oil'] = df.iloc[:,9]
df['(PADD 4) Refinery and Blender Net Input of Crude Oil'] = df.iloc[:,15]
df['(PADD 5) Refinery and Blender Net Input of Crude Oil'] = df.iloc[:,16]

df = df.iloc[:,-8:]

df['Total US Refinery Net Input of Crude Oil'] = df['(PADD 1) Refinery and Blender Net Input of Crude Oil'] + df['(PADD 2) Refinery and Blender Net Input of Crude Oil'] + df['(PADD 3) Refinery and Blender Net Input of Crude Oil'] + df['(PADD 4) Refinery and Blender Net Input of Crude Oil'] + df['(PADD 5) Refinery and Blender Net Input of Crude Oil']


# Preparing Quarter wise summary


quarter_1 = df.loc[df['Quarter']==1].sum()
quarter_2 = df.loc[df['Quarter']==2].sum()
quarter_3 = df.loc[df['Quarter']==3].sum()
quarter_4 = df.loc[df['Quarter']==4].sum()

quarter_wise_desc = pd.concat([quarter_1, quarter_2, quarter_3, quarter_4], axis=1)

quarter_wise_desc.drop(['Year', 'Month'], inplace = True)

quarter_wise_desc.iloc[0,0] = 1
quarter_wise_desc.iloc[0,1] = 2
quarter_wise_desc.iloc[0,2] = 3
quarter_wise_desc.iloc[0,3] = 4
quarter_wise_desc = quarter_wise_desc.T


quarter_wise_desc.to_csv('quarter_wise_summary.csv', index = False)

# Preparing year wise summary


year_first = df.loc[df['Year']==2016].sum()

year_wise_desc = year_first
year_wise_desc.iloc[0] = 2016

for year in range(2017, 2022):
    
    year_next = df.loc[df['Year']==year].sum()
    year_next.iloc[0] = year
    year_wise_desc = pd.concat([year_wise_desc, year_next], axis=1)
 
year_wise_desc.drop(['Quarter', 'Month'], inplace=True)

year_wise_desc = year_wise_desc.T

year_wise_desc.to_csv('year_wise_summary.csv', index = False)