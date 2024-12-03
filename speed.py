import csv

orionVX = []
orionVY = []
orionVZ = []

with open("newData.csv", newline='') as f:
    reader = csv.reader(f)
    data1 = list(reader)

    # Prints out the data, not needed now but good for debugging
#takes the data after the header so it starts at first number
    for line in data1[1:]:
    #gets the numbers in the first colum (the x)
        orionVX.append(line[4])
    print(orionVX)

#takes the data after the header so it starts at first number
    for line in data1[1:]:
    #gets numbers in the second colum (the y)
        orionVY.append(line[5])
    print(orionVY)

#takes the data after the header so it starts at first number
    for line in data1[1:]:
          #gets the numbersin the third colum (they z)
        orionVZ.append(line[6])
    print(orionVZ) 

