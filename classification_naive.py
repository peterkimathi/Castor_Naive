import pandas as pd
from Bio import SeqIO
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB,MultinomialNB, BernoulliNB
from sklearn.model_selection import train_test_split

gnb = GaussianNB()
multinb=MultinomialNB()
bernNB=BernoulliNB()


##Loading data
