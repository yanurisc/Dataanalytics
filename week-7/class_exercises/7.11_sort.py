# Yanuris Campusano
# 5/16/2026

# sort_index() and rank()

import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Student": ["Amy", "Bob", "Cara", "Dan"],
     "score": [88,95,79,91]
}, index=[3,1,2,0])

print("ORIGINAL DATAFRAME")
print(df)

# Sort by index 
print("/nSSORTED INDEX")
print(df.sort_index())

# Rank scores
df["Rank"] = df["score"].rank(ascending=False)

print("/nWITH RANKINGS")
print(df)


