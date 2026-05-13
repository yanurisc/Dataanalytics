def split_name(full_name):
    parts = full_name.split(" ")
    first = parts[0]
    last = parts[-1]
    return first, last

first, last = split_name("Bryan Williams")
print(f"First Name: {first}")
print(f"Last Name: {last}")


# split_name("Bryan Williams") = calls the function with a full name
# split(" ") = splits the name into ["Bryan", "Williams"]
# return first, last = returns both names
# print = displays each name separately