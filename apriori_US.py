#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:39:07 2020

@author: bhaskaryuvaraj
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
df = pd.read_excel('/Users/bhaskaryuvaraj/Downloads/Online Retail.xlsx')