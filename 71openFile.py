# Use words.txt as the file name
fname = input("Enter the File Name: ")
fh= open(fname)

for line in fh :
    line = line.rstrip()
    print(line.upper())
