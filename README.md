# KnowEnG's Gene Regulatory Network Pipeline
 This is the Knowledge Engine for Genomics (KnowEnG), an NIH BD2K Center of Excellence, Gene Regulatory Network Pipeline.

  
* * * 
## How to run this pipeline with Our data
* * * 
### 1. Get Access to KnowEnG-Research Repository:
Email omarsobh@illinois.edu infrastructure team (IST) lead to:

* __Access__ KnowEnG-Research github repo

### 2. Clone the Gene_Regulatory_Network Repo
```
 git clone https://github.com/KnowEnG-Research/Gene_Regulatory_Network.git
```
 
### 3. Install the following (Ubuntu or Linux)
```
 apt-get install -y python3-pip
 apt-get install -y libblas-dev liblapack-dev libatlas-base-dev gfortran
 pip3 install numpy==1.11.1
 pip3 install pandas==0.18.1
 pip3 install scipy==0.18.0
 pip3 install scikit-learn==0.17.1
 apt-get install -y libfreetype6-dev libxft-dev
 pip3 install matplotlib==1.4.2
 pip3 install pyyaml
 pip3 install knpackage
 pip3 install redis
```

### 4. Change directory to Gene_Regulatory_Network

```
cd Gene_Regulatory_Network 
```

### 5. Change directory to test

```
cd test
```
 
### 6. Create a local directory "run_dir" and place all the run files in it
```
make env_setup
```

### 7. Use following "make" commands to run a Gene Regulatory Network
```
make run_GRN
```


* * * 
## How to run this pipeline with Your data
* * * 

__***Follow steps 1-4 above then do the following:***__

### * Create your run directory

 ```
 mkdir run_directory
 ```

### * Change directory to the run_directory

 ```
 cd run_directory
 ```

### * Create your results directory

 ```
 mkdir results_directory
 ```
 
### * Create run_paramters file  (YAML Format)
 ``` 
Look for examples of run_parameters in ./Gene_Regulatory_Network/data/run_files/TEMPLATE_gene_regulatory.yml
 ```
### * Modify run_paramters file  (YAML Format)
```
set the spreadsheet file names to point to your data
```

### * Run the Gene Signature Pipeline:

  * Update PYTHONPATH enviroment variable
   ``` 
   export PYTHONPATH='../src':$PYTHONPATH    
   ```
   
  * Run
   ```
  python3 ../src/gene_regulatory.py -run_directory ./ -run_file TEMPLATE_gene_regulatory.yml
   ```

* * * 
## Description of "run_parameters" file
* * * 

| **Key**                   | **Value** | **Comments** |
| ------------------------- | --------- | ------------ |
| method                    | GRN_lasso | Calculate cosine similarity between two gene expression data |
| spreadsheet_name_full_path | directory+spreadsheet_name|  Path and file name of user supplied gene expression data  |
| alpha | 0.5| alpha parameter in Lasso regression |
| fit_intercept | True or False| fit_intercept parameter in Lasso regression  |
| normalize | True or False| normalize parameter in Lasso regression |
| results_directory | directory | Directory to save the output files |

spreadsheet_name_full_path = gene_spreadsheet_1.tsv</br>
* * * 
## Description of Output files saved in results directory
* * * 

* Output files


**GRN_coefficient_result.tsv**.</br>

|  | gene_1 | ... | gene_m |
|:---------:|:---------:|:---------:| :---------:|
| gene_1 | 1 | 0 | 0.5 |
| ... | ... | ... | ... | 
| gene_n | 0.1 | 0.2 | 1 |

