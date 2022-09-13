# data-enrichment
HHA 507 // Week 3 // Assignment 3

## this repo focuses on data enrichment with a focus on Hospital Inpatient Discharges (SPARCS) data acquired from: https://health.data.ny.gov/Health/Hospital-Inpatient-Discharges-SPARCS-De-Identified/82xm-y6g8
## data is downloaded in CSV for Excel format.

## this data will then be enriched by data taken from https://www.neighborhoodatlas.medicine.wisc.edu/.
## Users must register and navigate to the 'download data' section on the top-right corner of the site. Data format used in this project is '9-digit zip codes, New York, 2015.'


## this repo will mostly utilize pandas to perform merges and clean-up, using functions introduced in https://github.com/kezzhou/hha-data-cleanup
## for missing data, we may use numpy

## raw data files are placed in the 'raw' folder, which is not pushed to Github because of file size restrictions. Users looking to recreate the script should download raw files based on instructions provided above. Users should then create and place raw files under a new folder named 'data' under subfolder 'raw.' The final concatted or merged dataframe should be burned into folder 'data' subfolder 'enriched' with to_csv.
