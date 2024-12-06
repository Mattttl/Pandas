import pandas as pd
import numpy as np
exam_data = {'name': ["Matteo","Chardon","Diego","Denzel"],"grade":[50,90,2,-100],'attempts':[10,1,19,np.nan],'qualify':["no","yes","no","no"]}
labels = ['a','b','c','d']

df = pd.DataFrame(exam_data,index=labels)
print(df)
print(df.info())