# Cervical Cancer Screening
## Author: Kirsty Hawke

## Motivation

There is convincing evidence that the following factors increase your risk for cervical cancer.

* Infection with human papillomavirus (HPV)

* Sexual activity

* Smoking

* Giving birth many times

* Infection with human immunodeficiency virus (HIV)

* History of sexually transmitted infections (STIs)

* Oral contraceptives

* Diethylstilbestrol (DES)

 Source: https://cancer.ca/en/cancer-information/cancer-types/cervical/risks
 
 Cervical cancer is also one of the most preventable cancers and can be detected early with regular screening. Many developing countries continue to have high levels of cervical cancer due to lack of access and possibly anxiety and embarrassment. With this in mind, I decided to create an online cervical cancer screener that coud be accessed from a mobile phone or a computer. Feature engineering was key in the process of creating the webapp as it was vital to find a balance between collecting enough information for the model to perform well and limiting the amount of time needed to input the information.
 
## Data

The Cervical Cancer Risk Factors Dataset was published by researchers in Venezuela in 2017. It includes 32 features about 858 patients, ranging from age, smoking history to number of sexual partners and STDs. Many of the features were taken from self reported survey responses and there were many missing values. This dataset presented the challenge of being relatively small (less than 1000 rows) and many missing values (two features had over 80% of the data missing). Additionally, patients may under-report or omit certain values like the number of packs of cigarettes smoked per year and the questions relating to sexual activity.

There are four target variables: Hinselmann, Schiller, Cytology and Biopsy. Biopsy was chosen as the singular target as it is a common method of diagnosing cervical cancer. Around 1/8th of the patients had a positive result. For the final model, the positive class was upsampled.

![image](https://user-images.githubusercontent.com/32803881/156441516-98dd0a79-1151-4c90-9c41-bb5bff132532.png)

To deal with missing data, three imputation methods were explored:
* K Nearest Neighbour Imputation
* Most Frequent Value Imputation
* Automated Model Imputation (XGBoost & LightGBM)

Futhermore, to manage the amount of missing values I used RobustScalar which used statistics that are robust to outliers compared to StandardScalar.

Source: https://archive.ics.uci.edu/ml/datasets/Cervical+cancer+%28Risk+Factors%29#

## Feature Engineering

The number of features as well as how easily the user would have access to the information and how uncomfortable the user might be to respond to the questions was considered. However, a trial of a model using more conservative features did not perform as well as others. To understand the existing collinearities between features, a pearson ranking was performed:

![image](https://user-images.githubusercontent.com/32803881/156443560-b2e108b0-0c50-45a6-94fb-7f95960401d3.png)

These features are some of the strongest features correlated with each other:
    
* STDs:vulvo-perineal condylomatosis & STDs:condylomatosis
* STDs: Number of diagnosis & STDs (number)
* STDs: Time since first diagnosis & STDs: Time since last diagnosis
* Dx:Cancer & Dx:HPV
* Smokes & Smokes (years)

Feature importance was also considered. Below is the feature importances from KNN iputed data.

![image](https://user-images.githubusercontent.com/32803881/156444978-66c2d89d-cb8f-4c88-b6f6-afc444b5dbed.png)

Recursive feature elimination (RFE) was also explored to find a subset of features 

## Model

LightGBM and XGBoost were both considered however, LightGBM had a tendancy to overfit due to the small size of the dataset thus XGBoost was chosen. 

## Evaluation

## Results

Validation assessments:

https://www.mycanceriq.ca/Cancers/Cervical

https://www.cedars-sinai.org/health-library/risk-assessments/cervical-cancer-risk-assessment.html#:~:text=The%20American%20Cancer%20Society%20recommends,%2Dtesting)%20every%205%20years.

## Webapp


## Citations
https://www.hindawi.com/journals/sp/2021/5540024/tab1/
