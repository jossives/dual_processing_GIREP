# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 08:11:32 2014

@author: joss
"""

import numpy as np
import pandas as pd
import numpy as np

df = pd.read_csv('C:\Users\Joss\ownCloud\Shared_Read_Only\DP_Anonymized_Data\P100 - 2017-09\dpDatP100final.csv')

# Make sure the data look as I expect

print df.describe()

# Klugetastic: make a list, convert to an array and then a df
list2 = []

qnums = [5,6,13,14]
for index, row in df.iterrows():
    
    # 'index' is the row number
    # individual entries in the row can be indexed by row['ID'] as shown
    # print index, row['ID']
    
    # In a given row, I want to iterate over the questions
    # Recall that range(1,6) is actually iterate over 1-5
    for iq in qnums:
        question = 'A'+str(iq) 
        trtcol = 'A'+str(iq)+'.trt'
        qnumstring = 'P100.17W1.final.A'+str(iq)
        qnumstringshort = 'f0171.'+str(iq)
        course = 'P100'
        term = '2017W1'
        exam = 'final'
        
        # Leave blank if neither treatment nor control
        
        if row[trtcol]=='Treatment':
           treatment = 1
        elif row[trtcol]=='Control':
           treatment = 0
        else:
            treatment = ''

        # Leave blank if neither correct nor incorrect
        if row[question]>=1:
            qcorrect = 1
            list2.append([row['AnonID'], \
                      iq,qnumstring, qnumstringshort, course, term, exam, \
                      qcorrect, treatment, \
                      row['SoloTotal74'], \
                      row['Version'], row['Gender'], row['EYAinclude'], \
                      row['d.version'], row['NCRT'] \
                      ])               
        elif row[question]==0:
            qcorrect = 0
            list2.append([row['AnonID'], \
                      iq,qnumstring, qnumstringshort, course, term, exam, \
                      qcorrect, treatment, \
                      row['SoloTotal74'], \
                      row['Version'], row['Gender'], row['EYAinclude'], \
                      row['d.version'], row['NCRT'] \
                      ])        
        else:
            qcorrect = ''


# convert list2 to an array
array2 = np.array(list2)

colnames = ['ID','QNUM.0','QNUM.long','QNUM','COURSE','TERM','EXAM', \
    'QCORRECT','TREATMENT','SoloTotal74.F0', \
    'Version','Gender','EYAinclude','d.version','NCRT']

# now make a dataframe out of it
df2 = pd.DataFrame(array2,columns=colnames)

df2.to_csv('C:\Users\Joss\ownCloud\Shared\DP_Derived_Data\dpLogisticDat_P100F.csv',index=False,header=True)

### Script has finished successfully
print ""
print "Winner, winner, chicken dinner"