#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:20:13 2020

@author: bhaskaryuvaraj
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
by=pd.read_excel('/Users/bhaskaryuvaraj/Downloads/Online Retail.xlsx')
by['Country'].unique()
by.columns
by.isnull().sum()
#removing spaces in between
by['Description']=by['Description'].str.strip()

#creating new df by grouping and unstacking for only USA
ab=(by[by['Country']=='United Kingdom'].groupby(['InvoiceNo','Description'])['Quantity']
.sum().unstack().reset_index().fillna(0).set_index('InvoiceNo'))

#now changing the quantity of description to 0 is not purchased and 1 if purchased
def encode_units(x):
    if x<=0:
        return 0
    elif x>=0:
        return 1
    
by1=ab.applymap(encode_units)
by1.columns

#finding the support
support=apriori(by1, min_support=0.03, use_colnames=True)

#applying rules for lift
lift=association_rules(support,metric='lift',min_threshold=1)