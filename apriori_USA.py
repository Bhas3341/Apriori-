#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 21:22:43 2020

@author: bhaskaryuvaraj
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
by=pd.read_excel('/Users/bhaskaryuvaraj/Library/Mobile Documents/com~apple~CloudDocs/Documents/data_science work_files/Online Retail.xlsx')
by['Country'].unique()
by.columns
by.isnull().sum()
postage=by[by['Description']=='POSTAGE']
#removing spaces in between
by['Description']=by['Description'].str.strip()

#creating new df by grouping and unstacking for only USA
ab=(by[by['Country']=='USA'].groupby(['InvoiceNo','Description'])['Quantity']
.sum().unstack().reset_index().fillna(0).set_index('InvoiceNo'))

#now changing the quantity of description to 0 is not purchased and 1 if purchased
def encode_units(x):
    if x<=0:
        return 0
    elif x>=0:
        return 1
    
by1=ab.applymap(encode_units)
by1.columns
#by1.drop('POSTAGE',inplace=True,axis=1),since postage is unavilable
#finding the support
support=apriori(by1, min_support=0.07, use_colnames=True)
 
        
