array = [0,1,2,3,4,5,6,8,9]

len= len(array)
i = 0
while(i<len):
    if (array[i]==i):
        i=i+1
        continue
    else :
        print("Missing value is: ", i)
        break
