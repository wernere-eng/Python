# -*- coding: utf-8 -*-
"""
Created on Thu May  2 07:39:34 2019

@author: werne
"""

import numpy as np

my_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)

print(my_array)

ones_array = np.ones((3,4))
print(ones_array )

zero_array = np.zeros((2,3,4),dtype=np.int64)
print(zero_array)

empty_array = np.empty((4,4) ,dtype=np.int32)
print(empty_array)

