import csv

orionX = []
orionY = []
orionZ = []

with open("newData.csv", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    # Prints out the data, not needed now but good for debugging
#takes the data after the header so it starts at first number
    for line in data[1:]:
    #gets the numbers in the first colum (the x)
        orionX.append(line[1])
    print(orionX)

#takes the data after the header so it starts at first number
    for line in data[1:]:
    #gets numbers in the second colum (the y)
        orionY.append(line[2])
    print(orionY)

#takes the data after the header so it starts at first number
    for line in data[1:]:
          #gets the numbersin the third colum (they z)
        orionZ.append(line[3])
    print(orionZ) 

