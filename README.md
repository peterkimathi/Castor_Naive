# Using CASTOR for Virus Classification
We used Los Alamos to download the HIV data, and Gene Cutter to retreive POL dataset.
* Link to Los Alamos HIV Databases https://www.hiv.lanl.gov/content/index
* Link to Gene Cutter for Extracting POL https://www.hiv.lanl.gov/content/sequence/HIV/mainpage.html


#Comparison between Bayesian naive classification with logistic regression

|	Bayesian naive|logistic regression|	
|--------------|---------------|
|Both for classification Problems| Both for Classification Problems |
|Predition is poor when the features are dependent as the model assumes that all the features are conditionally independent |Performs wells even if the features are depended as the features are splitted linearly|
|Model the joint distribution of feature and target and predicts the posterior | Directly models the posterior regression of input against output and minimizing the errors|
