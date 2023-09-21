# Individual Project 1
[![Format](https://github.com/nogibjj/TianjiRao_Individual_Project_1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/TianjiRao_Individual_Project_1/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/TianjiRao_Individual_Project_1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/TianjiRao_Individual_Project_1/actions/workflows/install.yml)
[![Test](https://github.com/nogibjj/TianjiRao_Individual_Project_1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/TianjiRao_Individual_Project_1/actions/workflows/test.yml)
[![Lint](https://github.com/nogibjj/TianjiRao_Individual_Project_1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/TianjiRao_Individual_Project_1/actions/workflows/lint.yml)

IDS-706 Individaul Project 1 by Tianji Rao

## Video
https://www.youtube.com/watch?v=lyWqBmtPrHk

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
- `pd_visual(df)`

### Functions in `main.py`
Here we also design two functions that further package common functions in lib.py.
- `summary_desc()`
- `visual()`    
- `save_to_md()`

## Applications
### Testing Functions
- `test_summary_desc()` 
Checking mean, median, and standard deviation

- `test_visual()` 
- `test_save_to_md()`

### Testing Jupyter Notebook
Here we can use nvbal.

## Preparation
1. Setting up Codespaces
2. Check `make` operations

## Check format and test errors
1. Format `make format`
2. Lint `make lint`     
![Screenshot 2023-09-21 at 10 15 14 AM](https://github.com/nogibjj/TianjiRao_Individual_Project_1/assets/104114843/bbea3140-98de-4be9-a207-9acbd6ebd6bd)

3. Test `make test`
- Test `*.py`
<img width="849" alt="Screenshot 2023-09-19 at 2 49 47 PM" src="https://github.com/nogibjj/TianjiRao_Mini_Project_3/assets/104114843/6a4d40c4-5284-48d1-ae1d-467b47d2ff4d">

- Test `*.ipynb`
<img width="840" alt="Screenshot 2023-09-19 at 2 49 55 PM" src="https://github.com/nogibjj/TianjiRao_Mini_Project_3/assets/104114843/21a32244-290c-4093-9bbc-1dd9264430ff">


## Reference
https://pandas.pydata.org/    
https://catalog.data.gov/dataset/electric-vehicle-population-data
