## Script to parse cd-hit clstr file format to get clean Cluster","Entry format 
## Was tested with Python2 and CD-HIT version 4.7 (built on Mar 21 2018)

import pandas as pd

FILENAME="gene_calls_cat_90.clstr" # modify for the name of your cd-hit cluster file 

############# NO NEED TO MODIFY FROM HERE #############
fh = open(FILENAME) # file handle fh
df = pd.DataFrame() # init output dataframe

clstr="" # init
entr="" # init

while True:
    line = fh.readline()
    if line.startswith('>Cluster '): 
        clstr=line.split()[1]
    else:
        if line != "":
            entr=line.split('>')[1].split('...')[0]
            df = df.append({'cluster_id': clstr, 'entry': entr}, ignore_index=True)
    entr=""
    if not line:
        break
fh.close()

df.to_csv(FILENAME+".csv", sep=',', index=False) # output .csv file
