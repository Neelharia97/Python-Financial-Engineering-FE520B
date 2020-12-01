#Home Work 4 
# Author: Neel Haria


from pandas import DataFrame
import pandas as pd
import numpy as np


# In[2]:


#1 What is total amount spending captured in this dataset?
if __name__ == '__main__':
   #1 What is total amount spending captured in this dataset?

    res_purchase = pd.read_csv('res_purchase_2014.csv')
    #pd.set_option('display.max_columns',  None)
    res_purchase['Amount'] = res_purchase['Amount'].str.replace("$",'')
    res_purchase['Amount'] = res_purchase['Amount'].str.replace(",",'')
    res_purchase['Amount'] = res_purchase['Amount'].str.replace("(",'')
    res_purchase['Amount'] = res_purchase['Amount'].str.replace(")",'')
    res_purchase['Amount'] = res_purchase['Amount'].str.replace("zero",'')
    res_purchase['Amount'] = res_purchase['Amount'].fillna(0)
    res_purchase['Amount'] = res_purchase['Amount'].astype('float')
    print("The total amount spent is ${}".format(res_purchase['Amount'].sum().round(2)))
    #res_purchase['Amount'] 

    # In[4]:


    #2 & 3
    def total_vendor(Vendor):
        print("Total amount at {} is:".format(Vendor), res_purchase[res_purchase['Vendor']==Vendor]["Amount"].sum())
        


    # In[5]:


    #2. How much was spend at WW GRAINGER?
    total_vendor('WW GRAINGER')


    # In[6]:


    #3. How much was spend at WM SUPERCENTER?
    total_vendor('WM SUPERCENTER')


    # In[7]:


    #4. How much was spend at GROCERY STORES?
    def total_category(category):
        print("Total amount in {} category is:".format(category),res_purchase[res_purchase['Merchant Category Code (MCC)']==category]["Amount"].sum())
    total_category("GROCERY STORES,AND SUPERMARKETS")


    # In[ ]:



    #2Data Processing with Pandas (60 points)


    # In[42]:


    #1. Read ’Energy.xlsx’ and ’EnergyRating.xlsx’ as BalanceSheet and Ratings(dataframe).
    #2. drop the column if more than 90% value in this colnmn is 0 (or missing value).
    #3. replace all None or NaN with average value of each column.


    BalanceSheet = pd.read_excel('Energy.xlsx')
    pd.set_option('display.max_columns',  None)
    BalanceSheet = BalanceSheet.drop(columns=BalanceSheet.columns[((BalanceSheet==1).mean()>0.9)])
    BalanceSheet = BalanceSheet.fillna(BalanceSheet.mean()) #replacing all NaN values with mean 
    BalanceSheet = BalanceSheet.dropna(axis = 1, how = 'all') #replacing all columns with all NaN values
    print(BalanceSheet)


    # In[117]:


    #1. Read ’Energy.xlsx’ and ’EnergyRating.xlsx’ as BalanceSheet and Ratings(dataframe).
    #2. drop the column if more than 90% value in this colnmn is 0 (or missing value).
    #3. replace all None or NaN with average value of each column.


    Ratings = pd.read_excel('EnergyRating.xlsx')
    Ratings = Ratings.drop(columns=Ratings.columns[((Ratings==0).mean()>0.9)])
    Ratings = Ratings.fillna(Ratings.mean())#replacing all NaN values with mean 
    Ratings = Ratings.dropna(axis = 1, how = 'all')#replacing all columns with all NaN values
    print(Ratings)


    # In[51]:


    #4. Normalize the table
    BalanceSheet_cols = BalanceSheet.select_dtypes('float') #Normalization to applied only on Numerical Data
    Ratings_cols = Ratings.select_dtypes(np.number)


    # In[52]:


    #4. Normalize the table
    def x_new(x):
        a = (x-x.min())/(x.max()-x.min())
        return a
    Ratings_Normalized = Ratings_cols.apply(x_new)
    print(Ratings_Normalized)


    # In[116]:


    #4. Normalize the table
    BalanceSheet_Normalized = BalanceSheet_cols.apply(x_new)
    print(BalanceSheet_Normalized.dropna(axis = 1, how = 'all'))


    # In[57]:


    '''

    5. Define an apply function to return the statistical information for variables =
    [’Current Assets - Other - Total’, ’Current Assets - Total’, ’Other Long-termAssets’,
    ’Assets Netting & Other Adjustments’], you need to return a dataframe
    which has exactly same format with pandas method .describe().

    '''
    cor = pd.read_excel('Energy.xlsx')
    cor1 = cor[['Current Assets - Other - Total', 'Current Assets - Total', 'Other Long-term Assets','Assets Netting & Other Adjustments']]
    print(cor1.describe())
    #df_cor = df_cor[[’Current Assets - Other - Total’, ’Current Assets - Total’, ’Other Long-term
    #Assets’, ’Assets Netting  Other Adjustments’]


    # In[115]:


    '''

    6. Calculate the correlation matrix for variables = [’Current Assets - Other - Total’,
    ’Current Assets - Total’, ’Other Long-term Assets’, ’Assets Netting & Other
    Adjustments’].

    '''
    print(cor1.corr())


    # In[114]:


    '''
    7. If you look at column (’Company Name’), you will find some company name
    end with ’CORP’, ’CO’ or ’INC’. Create a new column (Name: ’CO’) to store
    the last word of company name. (For example: ’CORP’ or, ’CO’ or ’INC’) (Hint:
    using map function)

    '''

    BalanceSheet['CO'] = BalanceSheet['Company Name'].str.split().str[-1]
    print(BalanceSheet[['CO']])


    # In[ ]:





    # In[ ]:





    # In[113]:


    '''
    8. Merge (inner) Ratings and BalanceSheet based on ’datadate’ and ’Global Company
    Key’, and name merged dataset ’Matched’.

    '''

    matched = pd.merge(Ratings,BalanceSheet, on = ['Data Date', 'Global Company Key'],how = 'inner' )#on =  'Global Company Key')
    print(matched)


    # In[106]:


    '''
    9. Mapping
    For dataset ’Matched’, we have following mapping:
    AAA = 0
    AA+ = 1
    AA = 2
    AA- =3
    A+ = 4
    A = 5
    A- = 6
    BBB+ = 7
    BBB = 8
    BBB- = 9
    BB+ = 10
    BB = 11
    others = 12
    Using map function to create a new varible = ’Rate’, which maps ratings to
    numerical ratings.

    '''




    number_rating = {
        'AAA' : 0,
        'AA+' : 1,
        'AA' : 2,
        'AA-' :3,
        'A+' : 4,
        'A' : 5,
        'A-' : 6,
        'BBB+' :7,
        'BBB' : 8,
        'BBB-' : 9,
        'BB+' : 10,
        'BB' : 11,
        'others' :12,
        '':12
    }

    matched['Rate'] = matched['S&P Domestic Long Term Issuer Credit Rating'].map(number_rating) #mapping rate with number rating
    print(matched['Rate'])


    # In[112]:


    '''
    10. Calculate the rating frequency of company whose name end with ’CO’. (Calculate
    the distribution of rating given the company name ending with ’CO’, Hint,
    use map function)

    '''
    CO = matched[matched['CO'] == 'CO']
    RatingFrequency = CO['Rate'].mean()
    print("Rating Frequency of Companies ending with CO is {ratings}".format(ratings = RatingFrequency))


    # In[ ]:




