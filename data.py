import csv

orionX = []
orionY = []
orionZ = []
Ds54 = []
Ds54_data = []
Ds24 = []
Ds24_data = []
Ds34 = []
Ds34_data = []
orionVX = []
orionVY = []
orionVZ = []

#10 is where i need to start -Eddy 
with open("assets/data/newData.csv", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    # Prints out the data, not needed now but good for debugging
#takes the data after the header so it starts at first number
    for line in data[1:]:
    #gets the numbers in the first colum (the x)
        orionX.append(line[1])
    #print(orionX)

#takes the data after the header so it starts at first number
    for line in data[1:]:
    #gets numbers in the second colum (the y)
        orionY.append(line[2])
    #print(orionY)

#takes the data after the header so it starts at first number
    for line in data[1:]:
          #gets the numbersin the third colum (they z)
        orionZ.append(line[3])
    #print(orionZ) 

    for line in data[1:]:
        #gets numbers in tenth colum (if Ds54 is avaailable)
        Ds54.append(line[10])
    #print(Ds54)

    for line in data[1:]:
        #gets numbers in twelth colum (if Ds24 is avaailable)
        Ds24.append(line[12])
    #print(Ds24)

    for line in data[1:]:
        #gets numbers in fourteenth colum (if Ds34 is avaailable)
        Ds34.append(line[14])
    #print(Ds34)

    for line in data[1:]:
        #gets numbers in tenth colum (Data from Ds54)
        Ds54_data.append(line[11])
    #print(Ds54_data)

    for line in data[1:]:
        #gets numbers in twelth colum (Data from Ds24)
        Ds24_data.append(line[13])
    #print(Ds24_data)

    for line in data[1:]:
        #gets numbers in fourteenth colum (Data from Ds34)
        Ds34_data.append(line[15])
    #print(Ds34_data)
    for line in data[1:]:
    #gets the numbers in the first colum (the x)
        orionVX.append(line[4])
    print(orionVX)

#takes the data after the header so it starts at first number
    for line in data[1:]:
    #gets numbers in the second colum (the y)
        orionVY.append(line[5])
    print(orionVY)

#takes the data after the header so it starts at first number
    for line in data[1:]:
          #gets the numbersin the third colum (they z)
        orionVZ.append(line[6])
    print(orionVZ) 
