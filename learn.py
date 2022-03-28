import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Documents\\learning\\Consumer_Complaints.csv")

df = df.groupby('Product').count().reset_index()

df=df.sort_values()
