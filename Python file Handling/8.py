# Overwrite Existing Content


with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")
with open("demofile.txt") as f:
  print(f.read())