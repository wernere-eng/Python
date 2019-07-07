# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:09:39 2019

@author: werne
"""

import pandas as pd
import numpy as np


my_series  = pd.Series([1,3,5,np.nan,6,7])
print (my_series)


my_dates_index  = pd.date_range('20160101', periods=6) 
print(my_dates_index)

sample_numpy_data = np.array(np.arange(24)).reshape((6,4))
print(sample_numpy_data)


sample_df = pd.DataFrame(sample_numpy_data , index=my_dates_index , columns=list('ABCD'))
print(sample_df)
