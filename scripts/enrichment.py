#### terminal commands ####

'pip3 install pandas'

'pip3 install numpy'



#### import packages ####

from operator import concat
import pandas as pd

import numpy as np




#### import csv as dataframes ####

sparcs_df = pd.read_csv('data/raw/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv')

sparcs_df.sample

adi_df = pd.read_csv('data/raw/NY_2015_ADI_9 Digit Zip Code_v3.1.csv')

adi_df




#### pre merge clean-up ####

sparcs_df.columns

adi_df.columns

## in the interest of file size and functionality, let's drop a few columns from each df

sparcs_df = sparcs_df.drop(columns=['Patient Disposition', 'Discharge Year', 'APR Medical Surgical Description', 'Payment Typology 2', 'Payment Typology 3', 'Birth Weight', 'Abortion Edit Indicator', 'Emergency Department Indicator', 'Total Charges'])

sparcs_df.columns

adi_df = adi_df.drop(columns=['Unnamed: 0', 'X'])

adi_df.columns

## let's do some best practice cleaning with column names and element types

sparcs_df.columns = sparcs_df.columns.str.lower()

sparcs_df.columns

adi_df.columns = adi_df.columns.str.lower()

adi_df.columns

sparcs_df.columns = sparcs_df.columns.str.replace(' ', '_')

sparcs_df.columns

sparcs_df = sparcs_df.rename(columns={'payment_typology_1':'payment_typology'})
## now that we only have primary payment type left, we can drop the '1'

adi_df.columns = adi_df.columns.str.replace(' ', '_')

adi_df.columns

## let's try and shorten both tables by dropping rows from each. we may as well make them the same length

sparcs_df.drop(sparcs_df.loc[100:].index, inplace=True)

adi_df.drop(adi_df.loc[100:].index, inplace=True)

## the loc arguments of sparcs and adi start at differing points to account for NaN rows dropped in the following functions

sparcs_df.dropna(inplace=True)

adi_df.dropna(inplace=True)

## because this is a practice repo and these file sizes are huge, we can afford to drop rows with NaN

sparcs_df.shape

adi_df.shape

## sparcs and adi now contain the same amount of rows
## now we need to ensure that sparcs and adi's zipcode columns match
## adi's zipid is nine digits, which we need to shorten to first three to match sparcs'

# chopping zipid into first three digits
adi_df['zipid'] = adi_df['zipid'].str.slice(1, 4)

adi_df 

enrich_df = pd.concat([sparcs_df, adi_df])

enrich_df

enrich_df.to_csv('data/enriched/enrich.csv')

## with the new approach, merge gives an empty index and concat gives a stacked combined dataframe with NaN in certain sections
