



# Writing to a file
with open("student.txt", "w") as file:
    file.write("Alice\n")
    file.write("Bpb\n")
    
# Reading from a file
with open("students.txt", "r") as file:
    content = file.read ()
    print(content)
    
# Open file for reading
with open("example.txt", "r") as file:
    content = file.read()
    print(content)      
    
    # Open file for writing 
   with open("example.txt", "w") as file:
       file.write("Hello, python!")
       
       # Append text to a file
    with open  