import pandas as pd
import numpy as np
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv('Pipeline_Pytorch/data.csv')
print(df.head())
print(df.shape)
df.drop(columns=['id', 'unnamed:32'], inplace=True)