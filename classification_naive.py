from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB,MultinomialNB, BernoulliNB
import pandas as pd
from Bio import SeqIO
from sklearn.model_selection import train_test_split




gnb = GaussianNB()
multinb=MultinomialNB()
bernNB=BernoulliNB()




16S_data={}

for Sequence in SeqIO.parse("genecutter/Pol.na.fasta", "fasta",alphabet=None):
        16S_data[Sequence.id]=str(Sequence.seq).strip()


##Converting to pandas dataframe
df=pd. DataFrame(list(16S_data.items()))
training_data, testing_data = train_test_split(df, test_size=0.3, train_size=0.7, random_state=25)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
gnb = GaussianNB()
multinb=MultinomialNB()
bernNB=BernoulliNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
y_predM=multinb.fit(X_train, y_train).predict(X_test)
y_predB=bernNB.fit(X_train, y_train).predict(X_test)




print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_pred).sum()))
print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_predM).sum()))
print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_predB).sum()))
