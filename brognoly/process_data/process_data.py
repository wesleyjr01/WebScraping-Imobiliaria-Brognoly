import pandas as pd
import numpy as np

# Read .json file into a DataFrame
df = pd.read_json(r'C:\Users\wesle\brognoly\brognoly\spiders\sale_floripa_houses_brognoly.json',
                  orient='columns',encoding='utf-8')

# In[]:
df.info()


# In[]: Turn "Prices" into Floats
for i in range(len(df.Price)):
    df.loc[i,'Price'] = df.loc[i,'Price'][0][2:]
df.loc[:,'Price'] = df.loc[:,'Price'].astype(float)
df['Price_BRL'] = df.loc[:,'Price']
df['Price_1000BRL'] = df.loc[:,'Price_BRL']/1000
df.drop('Price', axis=1, inplace=True)


# In[]: Create features ('Dormitórios','Banheiros','Área[m²]','Vagas_Garagem')
string = df.realty_info.iloc[2]
substring = "Dormitórios"
 
df['Dormitorios'] = np.NaN
df['Banheiros'] = np.NaN
df['Area_m_2'] = np.NaN
df['Vagas_Garagem'] = np.NaN
for i in range(len(df.realty_info)): # para todos os exemplos
    for j in range(len(df.realty_info[i])): # para cada string dentro da lista
        if ("Dormitórios"  in df.realty_info[i][j]) | ("Dormitório"  in df.realty_info[i][j]):
        	df.loc[i,'Dormitorios'] = df.realty_info[i][j].rsplit(' ')[0]
        elif ("Banheiros" in df.realty_info[i][j]) | ("Banheiro" in df.realty_info[i][j]):
            df.loc[i,'Banheiros'] = df.realty_info[i][j].rsplit(' ')[0]
        elif "m²" in df.realty_info[i][j]:
            df.loc[i,'Area_m_2'] = df.realty_info[i][j].rsplit(' ')[0]
        elif ("Vagas" in df.realty_info[i][j]) | ("Vaga" in df.realty_info[i][j]):
            df.loc[i,'Vagas_Garagem'] = df.realty_info[i][j].rsplit(' ')[0]
df.loc[:,'Dormitorios'] = df.loc[:,'Dormitorios'].astype(float)
df.loc[:,'Banheiros'] = df.loc[:,'Banheiros'].astype(float)
df.loc[:,'Area_m_2'] = df.loc[:,'Area_m_2'].astype(float)
df.loc[:,'Dormitorios'] = df.loc[:,'Dormitorios'].astype(float)

# In[]: Rearrange 'Neighborhood' feature, and create 'City' feature
df['City'] = np.NaN
for i in range(len(df.neighborhood)):
    neigh = df.loc[i,'neighborhood'][0].rsplit(',')[0]
    df.loc[i,'City'] = df.loc[i,'neighborhood'][0].rsplit(',')[1][1:]
    df.loc[i,'neighborhood'] = neigh
# In[]:
df.info()

# In[]: Write output as json file
df.to_json(r'C:/Users/wesle/brognoly/brognoly/spiders/df_sale_floripa_houses_brognoly.json',orient='records')

# In[]: Write output as csv file
df.to_csv(r'C:/Users/wesle/brognoly/brognoly/spiders/df_sale_floripa_houses_brognoly.csv',index=False)

# In[]: Read csv test
#df3 = pd.read_csv(r'C:/Users/wesle/brognoly/brognoly/spiders/df_sale_floripa_apartments_brognoly.csv', header=0)