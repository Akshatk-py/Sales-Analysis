import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

sales = pd.read_csv('./Data/CSV AND EXCELS/Sales_Data/Combined Sales.csv')
# =================TO COMBINE ALL DATA FILES=========================================
# filepaths = [f for f in os.listdir("./Data/CSV AND EXCELS/Sales_Data/")]
# df = pd.DataFrame();sales= pd.DataFrame()
# for files in filepaths:
#     df = pd.read_csv('./Data/CSV AND EXCELS/Sales_Data/' + files)
#     sales = pd.concat([sales,df])
#     
# =============================================================================

# ======================TO DELETE THE UNWANTED ROWS====================================
# sales = sales.drop(sales.index[1])
# 
# c = list()
# for i in range(len(sales.iloc[0:])):
#     if sales.iloc[i][0] == 'Order ID':
#         c.append(i)
# sales
# sales = sales.drop(sales.index[c[:]])
# sales.to_csv('./Data/CSV AND EXCELS/Sales_Data/Combined Sales.csv',index = False)
# =============================================================================
sales['Sales'] = 0
sales['Sales'] = sales['Quantity Ordered'] * sales['Price Each']
sales['Month'] = 0
print(sales.loc[sales['Order Date'] == '04/19/19 08:46'])
sales['Month'] = sales['Order Date'].str.split('/')
sales.Month = sales.Month.str[0]
sales.head(10)
sales['Date'] = sales['Order Date'].str.split('/')
sales.Date = sales.Date.str[1]
sales['Year'] = sales['Order Date'].str.split('/')
sales['Year'] = sales['Year'].str[2]
sales.Year = sales.Year.str.split(' ')
sales.Year = sales.Year.str[0]

sales.Year = pd.to_numeric(sales.Year)
sales.Sales = pd.to_numeric(sales.Sales)
sales.Month = pd.to_numeric(sales.Month)
sales['City'] = 0;sales['cityass'] = 0
sales['City'] = sales['Purchase Address'].str.split(',')
sales['cityass'] =sales['City'].str[2] 
sales['cityass'] = sales['cityass'].str.split(' ')
sales['cityass'] =sales['cityass'].str[1] 
sales['City'] = sales['City'].str[1] + ' ' + sales.cityass
sales['City'].head(30)
#sales = sales.drop(sales.index[355])

city_dict = list()
city_dict = sales.City.unique()
city_sales_list = dict()

#-------------------------TO GIVE EVERY CITY ITS TOTAL SALES----------------------------------
for k in city_dict:
    city_sales_list[k] =  sales.loc[sales['City'] == k,'Sales'].sum()
#----------------------TO Drop Nan values in the DataFrame (Self Exprimented)--------------
sales = sales.drop(sales.loc[sales['City'] == k,'Sales'].index) #TOO IMPORTANT
#-----------------------------K == None or Nan-----(IGNORE INTELLISENSE RED CORRECTION)-------------------------------------------------------
    
for j,k in city_sales_list.items():
    plt.bar(j,k)
plt.xticks(rotation = 90)
# ===============IMPROVMENT OF BELOW CODE SHOW IN ABOVE CODE IN LINE(59-60)============================================
# city_dict = list()
# city_dict = sales.City.unique()
# city_sales_list = np.arange(1,len(city_dict)+1,1,'float64')
# city_sales_list[:] = 0 
# for i in range(len(sales.City.iloc[:])):
#     if sales['City'].iloc[i] == ' Dallas TX':
#         city_sales_list[0] += sales.Sales.iloc[i]
#     if sales['City'].iloc[i] == ' Boston MA':
#         city_sales_list[1] += sales.Sales.iloc[i]
#     if sales['City'].iloc[i] == ' Los Angeles CA':
#         city_sales_list[2] += sales.Sales.iloc[i]
#     if sales['City'].iloc[i] == ' San Francisco CA':
#         city_sales_list[3] += sales.Sales.iloc[i]
#     if sales['City'].iloc[i] == ' Seattle WA':
#         city_sales_list[4] += sales.Sales.iloc[i]
#     if sales['City'].iloc[i] == ' Atlanta GA':
#         city_sales_list[5] += sales.Sales.iloc[i]
#     if sales['City'].iloc[i] == ' New York City NY':
#         city_sales_list[6] += sales.Sales.iloc[i]
#     if sales['City'].iloc[i] == ' Portland OR':
#         city_sales_list[7] += sales.Sales.iloc[i]
#     if sales['City'].iloc[i] == ' Austin TX':
#         city_sales_list[8] += sales.Sales.iloc[i]
#     if sales['City'].iloc[i] == ' Portland ME':
#         city_sales_list[9] += sales.Sales.iloc[i]
# =============================================================================


#----------------------Monthly Sales----------------------------------------------
Month_dict = list()
Month_dict = sales.Month.unique()
Monthly_sales_list = dict()
for k in Month_dict:
    Monthly_sales_list[k] =  sales.loc[sales['Month'] == k,'Sales'].sum()
for j,k in Monthly_sales_list.items():
    plt.bar(j,k)
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])

#------------------------Yearly Sales--------------------------------------------
Year_dict = list()
Year_dict = sales.Year.unique()
Yearly_sales_list = dict()
for k in Year_dict:
    Yearly_sales_list[k] =  sales.loc[sales['Year'] == k,'Sales'].sum()
    
for j,k in Yearly_sales_list.items():
    plt.plot(j,k)
plt.xticks(rotation = 90)

#---------------------------Product-Wise Sales----------------------------------
Product_dict = list()
Product_dict = sales.Product.unique()
Product_sales_list = dict()
for k in Product_dict:
    Product_sales_list[k] =  sales.loc[sales['Product'] == k,'Sales'].sum()
    
for j,k in Product_sales_list.items():
    plt.bar(j,k)
plt.xticks(rotation = 90)

#-----------------------Dallas TX_Sales(PRODUCT WISE)-------------------------------
Dallas_dict = list()
Dallas_dict = sales.Product.unique()
Dallas_sales_list = dict()
for k in Dallas_dict:
    Dallas_sales_list[k] =  sales.loc[(sales['Product'] == k) & (sales['City'] == ' Dallas TX'), 'Sales'].sum()
plt.title('Dallas TX_Sales')
plt.xlabel('Products')
plt.ylabel('Sales(U.S.D $')

for j,k in Dallas_sales_list.items():
    plt.bar(j,k)
plt.xticks(rotation = 90)

#------------------------San Francisco CA_Sales(PRODUCT WISE)------------------------------
sf_dict = list()
sf_dict = sales.Product.unique()
sf_sales_list = dict()
for k in sf_dict:
    sf_sales_list[k] =  sales.loc[(sales['Product'] == k) & (sales['City'] == ' San Francisco CA'), 'Sales'].sum()
    
plt.title('San Francisco CA_Sales')
plt.xlabel('Products')
plt.ylabel('Sales(U.S.D $')

for j,k in sf_sales_list.items():
    plt.bar(j,k)
plt.xticks(rotation = 90)

#---------------------------Portland ME_Sales(PRODUCT WISE)------------------------------
Pme_dict = list()
Pme_dict = sales.Product.unique()
Pme_sales_list = dict()
for k in Pme_dict:
    Pme_sales_list[k] =  sales.loc[(sales['Product'] == k) & (sales['City'] == ' Portland ME'), 'Sales'].sum()
    
plt.title('Portland ME_Sales')
plt.xlabel('Products')
plt.ylabel('Sales(U.S.D $')

for j,k in Pme_sales_list.items():
    plt.bar(j,k)
plt.xticks(rotation = 90)

#---------------------------New York City NY_Sales(PRODUCT WISE)------------------------------
NY_dict = list()

NY_sales_list = dict()
for k in NY_dict:
    NY_sales_list[k] =  sales.loc[(sales['Product'] == k) & (sales['City'] == ' New York City NY'), 'Sales'].sum()
    
plt.title('New York City NY_Sales')
plt.xlabel('Products')
plt.ylabel('Sales(U.S.D $')

for j,k in NY_sales_list.items():
    plt.bar(j,k)
plt.xticks(rotation = 90)

#---------------------------Portland OR_Sales(PRODUCT WISE)------------------------------
POR_dict = list()
POR_dict = sales.Product.unique()
POR_sales_list = dict()
for k in POR_dict:
    POR_sales_list[k] =  sales.loc[(sales['Product'] == k) & (sales['City'] == ' Portland OR'), 'Sales'].sum()
    
plt.title('Portland OR_Sales')
plt.xlabel('Products')
plt.ylabel('Sales(U.S.D $')

for j,k in POR_sales_list.items():
    plt.bar(j,k)
plt.xticks(rotation = 90)

#---------------------------Atlanta GA_Sales(PRODUCT WISE)------------------------------
AGA_dict = list()
AGA_dict = sales.Product.unique()
AGA_sales_list = dict()
for k in AGA_dict:
    AGA_sales_list[k] =  sales.loc[(sales['Product'] == k) & (sales['City'] == ' Atlanta GA'), 'Sales'].sum()
    
plt.title('Atlanta GA_Sales')
plt.xlabel('Products')
plt.ylabel('Sales(U.S.D $')

for j,k in AGA_sales_list.items():
    plt.bar(j,k)
plt.xticks(rotation = 90)

#---------------------------Los Angeles_Sales(PRODUCT WISE)------------------------------
LA_dict = list()
LA_dict = sales.Product.unique()
LA_sales_list = dict()
for k in LA_dict:
    LA_sales_list[k] =  sales.loc[(sales['Product'] == k) & (sales['City'] == ' Los Angeles CA'), 'Sales'].sum()
    
plt.title(' Los Angeles CA_Sales')
plt.xlabel('Products')
plt.ylabel('Sales(U.S.D $')

for j,k in LA_sales_list.items():
    plt.bar(j,k)
plt.xticks(rotation = 90)

#---------------------------Boston_Sales(PRODUCT WISE)------------------------------
Boston_dict = list()
Boston_dict = sales.Product.unique()
Boston_sales_list = dict()
for k in Boston_dict:
    Boston_sales_list[k] =  sales.loc[(sales['Product'] == k) & (sales['City'] == ' Boston MA'), 'Sales'].sum()
    
plt.title(' Boston MA_Sales')
plt.xlabel('Products')
plt.ylabel('Sales(U.S.D $')

for j,k in Boston_sales_list.items():
    plt.bar(j,k)
plt.xticks(rotation = 90)
