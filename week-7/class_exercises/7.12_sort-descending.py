# Yanuris Campusano
# 5/16/2026

# sort_index() and rank()
# display result in descending 

import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Student": ["Amy", "Bob", "Cara", "Dan"],
    "Score": [88, 95, 79, 91]
}, index=[3,1,2,0])

print("ORIGINAL DATAFRAME")
print(df)
print()


# Sort index from highest to lowest


print("/nSORTED INDEX (Highest to lowest)")
sorted_df = df.sort_index(ascending=False)

print(sorted_df)


# Rank scores from highest to lowest


df["Rank"] = df["Score"].rank(ascending=False)

 # Sort by rank so highest score appears first
ranked_df = df.sort_values(by="Rank")
 
print("/nRANKINGS (Highest to Lowest)")
print(ranked_df)
 
