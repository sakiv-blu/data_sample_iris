import pandas as pd
import sys

df = pd.read_csv(sys.stdin)
df = df['DATE']

df.to_csv(sys.stdout, index = False)