# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 08:11:32 2014

@author: joss
"""

import numpy as np
import pandas as pd
import numpy as np

df = pd.read_csv('C:\Users\Joss\ownCloud\Shared_Read_Only\DP_Anonymized_Data\P101 - 2018-01\dpDat.csv')

# Make sure the data look as I expect

print df.describe()

# Klugetastic: make a list, convert to an array and then a df
list2 = []

for index, row in df.iterrows():
    
    # 'index' is the row number
    # individual entries in the row can be indexed by row['ID'] as shown
    # print index, row['ID']
    
    # In a given row, I want to iterate over the questions
    # Recall that range(1,6) is actually iterate over 1-5
    for iq in range(1,21):
        question = 'f.A'+str(iq) 
        trtcol = 'f.A'+str(iq)+'.trt'
        # Leave blank if neither treatment nor control
        if (iq==5) or (iq==6) or (iq==9) or (iq==10):
            if row[trtcol]=='Treatment':
                treatment = 1
            elif row[trtcol]=='Control':
                treatment = 0
            else:
                treatment = ''
        else:
            treatment = 0

        #if row[gr] > 0:
        #    trt = 1
        #else:
        #    trt = 0
        
        #print row['ID'],row[post],row['GROUPID'],trt,row[gr],row[pre]

        # Leave blank if neither correct nor incorrect
        if row[question]>=1:
            qcorrect = 1
            list2.append([row['AnonID'], \
                      iq,qcorrect, treatment \
                      ])
        elif row[question]==0:
            qcorrect = 0
            list2.append([row['AnonID'], \
                      iq,qcorrect, treatment \
                      ])        
        else:
            qcorrect = ''


# convert list2 to an array
array2 = np.array(list2)

colnames = ['ID','QNUM','QCORRECT','TREATMENT']
# now make a dataframe out of it
df2 = pd.DataFrame(array2,columns=colnames)

df2.to_csv('C:\Users\Joss\ownCloud\Shared\DP_Derived_Data\dpLogisticDat.csv',index=False,header=True)

### Script has finished successfully
print ""
print "Winner, winner, chicken dinner"