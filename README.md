# Individual Project 1
IDS-706 Individaul Project 1 by Tianji Rao

## **Report**

This repo contains:   
- .devcontainer     
- .github   
- .gitignore    
- Makefile  
- README.md     
- requirements.txt   
- `lib.py`    
- `test_lib.py`      
- `main.py`   
- `test_main.py`  
- Eletric_Vechile_Population_Data.csv  (Dataset)    
- some `.sh` files


## Purpose
The purpose of this project is using the `Pandas` to show statistics descriptions. The author use a `pd.DataFrame` as a sample data and test its descriptions. 


## Dataset
The experimental dataset is Eletric Vehicle Population Data that provided by DATA.GOV. Here I downloaded the .csv file and made it the dataset for testing.
The url address is https://catalog.data.gov/dataset/electric-vehicle-population-data. 
I used `pd.read_csv()` to read this dataset and save as a `pd.DataFrame`.

## Functions
### Functions in `lib.py`
- `pd_desc(df)` 
- `mean(df)`    
- `median(df)`  
- `std(df)`

### Functions in `main.py`
Here we also design two functions that further package common functions in lib.py.
- `summary_desc(df)`
- `desc_pd(df)`


## Applications
### Testing Functions
- `test_summary_desc()` 
Checking mean, median, and standard deviation

### Testing Jupyter Notebook
Here we can use 

## Preparation
1. Setting up Codespaces
2. Check `make` operations

## Check format and test errors
1. Format `make format`
2. Lint `make lint`     


3. Test `make test`     
- Test `*.ipynb`
<img width="1253" alt="Screenshot 2023-09-19 at 2 34 36 PM" src="https://github.com/nogibjj/TianjiRao_Mini_Project_3/assets/104114843/f3741877-6010-4ffc-84ac-570b02321762">

- Test `*.py`
<img width="1256" alt="Screenshot 2023-09-19 at 2 34 24 PM" src="https://github.com/nogibjj/TianjiRao_Mini_Project_3/assets/104114843/3c235ce0-fc8a-4e9b-bd38-a2f8936e8d15">

## Reference
https://pandas.pydata.org/    
https://catalog.data.gov/dataset/electric-vehicle-population-data