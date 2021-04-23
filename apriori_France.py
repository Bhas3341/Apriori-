#Install mlxtend and apriori
#Install mlxtend using belwo comand in conda, if it doesn't exist in spyder
#conda install -c conda-forge mlxtend 
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
df = pd.read_excel('/Users/bhaskaryuvaraj/Library/Mobile Documents/com~apple~CloudDocs/Documents/data_science work_files/Online Retail.xlsx')
df1=df
df.shape
df.head()
df.tail()

df.dtypes
#some of the descriptions have spaces that need to be removed
df['Description'] = df['Description'].str.strip()

#Check if an invoice number is missing
df.isnull().sum()

#drop the rows that don’t have invoice numbers
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)

#consolidate the items into 1 transaction per row with each product
#Looking at sales for France only for ease
basket = (df[df['Country'] =="France"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))
# Check how does data look after transformation
basket.to_excel('C:\\M U K E S H\\T R A I N I N G\\PYTHON\\CODES\\Association Rule\\France_Encoded_Data.xlsx')

# Encode -ve or 0 value transaction to 0 and +ve one to 1
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
    
# Apply Encoding
basket_sets = basket.applymap(encode_units)
basket_sets.to_excel('C:\\M U K E S H\\T R A I N I N G\\PYTHON\\CODES\\Association Rule\\France_Encoded_Data.xlsx')

#Delete POSTAGE item from the data. It is included in many bills to add postage charge
basket_sets.drop('POSTAGE', inplace=True, axis=1) 

#generate frequent item sets that have a support of at least 7% 
#(this number was chosen so that I could get enough useful examples)
frequent_itemsets = apriori(basket_sets, min_support=0.07, use_colnames=True)

#The final step is to generate the rules with their corresponding support, confidence and lift:
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.head()

rules.to_excel('C:\\M U K E S H\\T R A I N I N G\\PYTHON\\CODES\\Association Rule\\France_rules.xlsx')

#We can filter the dataframe using standard pandas code. 
#In this case, look for a large lift (6) and high confidence (.8):
recommended_combo=rules[ (rules['lift'] >= 4) & (rules['confidence'] >= 0.7) ]