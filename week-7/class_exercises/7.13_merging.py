# Yanuris Campusano
# 5/16/2026

# merging dataframes 

import pandas as pd   # import pandas library


#DataFrame 1: Students 

students = pd.DataFrame({
    "StudentID": [1,2,3,4],  # student ID numbers 1 through 4
    "Name": ["Amy", "Bob", "Cara", "Dan"] # each student's name
    })


# DataFrame 2: Scores
scores = pd.DataFrame({   # create the students table
    "StudentID": [1, 2, 3, 5], # note: ID 4 (Dan) is missing, ID 5 is extra
    "Score": [85, 92, 78, 88]  # each student's score
})

print("STUDENTS DATAFRAME") # label for students table
print(students) # show the students table

print("/nSCORES DATAFRAME") # label for scores table
print(scores) # show the scores table

print()
# print a blank line for spacing


 # 1. INNER JOIN (default)
 
inner_merge = pd.merge(students,scores, on="StudentID", how="inner") # Merge students and scores - only keep students WITH a score
print("/nINNER MERGE (only matching StudentID)") # label for output
print(inner_merge) # show the result


# 2. LEFT JOIN 

left_merge = pd.merge(students, scores, on="StudentID", how="left") # Merge students and scores - keep ALL students even if no score
print("/nLEFT MERGE (all students kept)")  # label for output
print(left_merge) # show the result


# 3. RIGHT JOIN

right_merge = pd.merge(students, scores, on="StudentID", how="right") # Merge students and scores - keep ALL scores even if no student match
print("/nRIGHT MERGE (all scores kept)") # label for output
print(right_merge) # show the result


# 4. OUTER JOIN

outer_merge = pd.merge(students, scores, on="StudentID", how="outer") # Merge students and scores - keep EVERYTHING from both tables
print("/nOUTER MERGE (all data from both)")  # label for output
print(outer_merge) # show the result

