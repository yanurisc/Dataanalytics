# Yanuris Campusano 
# 5/16/2026     

# Panda statistical functions

import pandas as pd

data = {
    "Student" :["Amy", "Bob", "Cara", "Dan", "Eva"],
    "Score":[85,92,78,95,100]
}

df = pd.DataFrame(data)
print(df)
print()

print("SUM:", df["Score"].sum())
print("COUNT:", df["Score"].count())
print("MEAN:", df["Score"].mean())
print("MEDIAM:", df["Score"].median())
print("MIN:", df["Score"].min())
print("MAX:", df["Score"].max())

print("/nAggregate Results:")
print(df["Score"].agg(["sum", "mean", "median","min", "max"]))
