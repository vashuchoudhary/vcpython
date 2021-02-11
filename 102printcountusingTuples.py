fname = input("Enter the filename: ")
if len(fname) < 1 : name = "mbox-short.txt"

fh = open(fname)
lst = list()
time = list()
hour = list()
valuekey = list()
count = dict()
for line in fh :
    if line is None or len(line)<5:
        continue
    if line.startswith("From "):
            lst = line.split()
            time.append(lst[5])

#print("Printing list of time")
#print(time)
#creating the touples of time and how many time they occurred
for times in time:
    times = times.split(':')
    #print("times array: ", times)
    #for hr in times[0]:
    count[times[0]] = count.get(times[0],0) + 1

#print("Printing the count histogram of hour")
#print(count)
#print("Printing coint.items(): ",count.items())

#need to print them now in reverse order:
for k,v in sorted(count.items()):
    print(k,v)
    #valuekey.append((k,v))
