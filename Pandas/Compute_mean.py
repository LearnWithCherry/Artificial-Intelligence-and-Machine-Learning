import pandas as pd

data = {"Name": ["A", "B", "C"], "Age": [20, 25, 22]}
df = pd.DataFrame(data)

print(df)
print(df["Age"].mean())
