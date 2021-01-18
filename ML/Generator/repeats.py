import os

path = os.path.dirname(__file__)


print("Opening File")
infile = path+"/data.txt"

arr = set()
with open(infile, 'r', encoding='utf-8') as f:
    line = f.readline()

    while line:
        arr.add(line)
        line = f.readline()

arr = list(arr)

tmp = []
print("Modifying File")
for i in range(len(arr)):
    line = arr[i]
    if "("  in line or "[" in line:
        continue

    tmp.append(line)
    
arr = tmp

print("Writing File")
outfile = path+"/dataout.txt"

with open(outfile, 'w', encoding='utf-8') as f:
    for i in range(len(arr)):
        f.write(arr[i])


    