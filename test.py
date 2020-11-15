# %%
import pandas as pd
import numpy as np
import os

# %%
os.listdir()
data = {"col_1": [3, 2, 1, 0], "col_2": ["a", "b", "c", "d"]}
pd.DataFrame.from_dict(data)
