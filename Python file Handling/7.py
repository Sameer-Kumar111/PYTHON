# Write to an Existing File


with open("demofile.txt", "a") as f:
    f.write("Student Now the file has more content")
with open("demofile.txt") as f:
    print(f.read())
    
    
    
    

