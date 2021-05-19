in_ = input("Enter input file directory... ")
out = input("Enter output file name... ")
dictionary = []

with open(in_) as file:
  for i in file.read().split(" "):
    if i not in dictionary:
      dictionary.append(i)

open(out, "w").close()

with open(out, "a+") as outfile:
  for i in dictionary:
    outfile.write(i + "\n")
  outfile.write("\n")
  with open(in_) as infile:
    infile.seek(0)
    temp = infile.read()
    for i in dictionary:
      temp = temp.replace(i, str(dictionary.index(i)))
    outfile.write(temp)
