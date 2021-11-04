import pandas as pd
from Bio import SeqIO
from sklearn.model_selection import train_test_split
import sys,os

##Dict for storing the fasta files
data={}
for Sequence in SeqIO.parse("input/Pol.na.fasta", "fasta",alphabet=None):
	data[Sequence.id]=str(Sequence.seq).strip()


##Converting Dict to pandas dataframe
df=pd. DataFrame(list(data.items()))

print(df.head())


##Divide the dataset in two parts: 80% for training (Dataset E) and 10% for testing (Dataset T)

training_data, testing_data = train_test_split(df, test_size=0.1, train_size=0.8, random_state=25)


##Confirming the length of the entries
print(len(training_data), len(testing_data))

##Create Test and Training fasta files
def create_fasta(dat, out):
	fin=open(out, "wt")
	for j in dat.itertuples():
		dt=j[1].split(".")
		ID=">"+dt[-1]+"|"+dt[0]+"_"+dt[1]
		SEQ=j[2]
		fin.write(ID+"\n")
		fin.write(SEQ+"\n")
	fin.close()

create_fasta(training_data, "input/training_data.fasta")
create_fasta(testing_data, "input/testing_data.fasta")
#Run CASTOR with default parameters in the config file
os.system("python main.py configuration_file.ini")
