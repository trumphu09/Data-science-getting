import pandas as pd
import numpy as np

df = pd.read_csv("chipotle.tsv", sep = "\t")
print(df.head(5))