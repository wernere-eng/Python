# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:13:52 2019

@author: werne
"""

import numpy as np
import pandas  as pd


##############################################
# country events
dataset = pd.read_csv('pandas_tutorial_read.csv' , delimiter = ';' , names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])

print(dataset.head(20))

print(dataset.sample(5))

print(dataset.tail(20))

print(dataset[['country' , 'user_id']])

print(dataset[dataset.source == 'SEO'])

print(dataset.head(10)[['country',  'user_id']])

print(dataset[['country' , 'user_id']].head(20))

print(dataset.groupby(['source' ,'topic']).count()[['user_id']])

###############################################
#zoo

zoo_data = pd.read_csv('zoo.csv', delimiter = ',')
print(zoo_data[['animal']].count())

print(zoo_data.water_need.sum())

print(zoo_data.water_need.median())
print(zoo_data.water_need.mean())

print(zoo_data.groupby('animal').mean()[['water_need']])

zoo_eats = pd.DataFrame([['elephant','vegetables'], ['tiger','meat'], ['kangaroo','vegetables'], ['zebra','vegetables'], ['giraffe','vegetables']], columns=['animal', 'food'])

print(zoo_eats)

print(zoo_data.merge(zoo_eats))

print(zoo_data.merge(zoo_eats , how = 'left' , left_on = 'animal' , right_on = 'animal'))

