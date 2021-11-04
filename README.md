# Using CASTOR for Virus Classification
We used Los Alamos to download the HIV data, and Gene Cutter to retreive POL dataset.
* Link to Los Alamos HIV Databases https://www.hiv.lanl.gov/content/index
* Link to Gene Cutter for Extracting POL https://www.hiv.lanl.gov/content/sequence/HIV/mainpage.html
* To run the script, type the following
* python run_all.py
* When prompted, select option 1, then 2, then 3 and finally four.

# Castor Classification Results 
|Subtype| precision |   recall  |f1-score  | support|
|-----------|-----------|-----------|-----------|-----------|
|HIV-1_01B  |     0.00 |     0.00  |    0.00  |       1|
|HIV-1_01_AE |      1.00 |     1.00 |     1.00 |        9|
|HIV-1_02A1  |     0.00  |    0.00  |    0.00  |       1|
|HIV-1_02_AG |      0.33 |     1.00  |    0.50 |        1|
|HIV-1_30_0206 |      0.00|      0.00 |     0.00 |        1|
|HIV-1_35_A1D |      1.00 |     1.00  |    1.00  |       1|
|HIV-1_69_01B |      0.00|      0.00  |    0.00|         0|
|HIV-1_A1   |    1.00  |    1.00  |    1.00   |      3|
|HIV-1_B   |    1.00 |     1.00  |    1.00  |      30|
|HIV-1_C  |     1.00 |     1.00  |    1.00 |        2|
|HIV-1_G  |     0.00  |    0.00  |    0.00 |        0|
|HIV-1_U  |     0.00   |   0.00  |    0.00  |       1|
|         |             |         |         |         |
|accuracy  |             |       |    0.92  |      50|
|macro avg  |     0.44   |   0.50  |    0.46  |     50|
|weighted avg |      0.91  |    0.92 |      0.91 |     50|



#Comparison between Bayesian naive classification with logistic regression

|	Bayesian naive|logistic regression|	
|--------------|---------------|
|Both for classification Problems| Both for Classification Problems |
|Predition is poor when the features are dependent as the model assumes that all the features are conditionally independent |Performs wells even if the features are depended as the features are splitted linearly|
|Model the joint distribution of feature and target and predicts the posterior | Directly models the posterior regression of input against output and minimizing the errors|
