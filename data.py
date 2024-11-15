import csv

#f = open("nasaadc-main/data.csv", "r")

with open("newData.csv", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    # Prints out the data, not needed now but good for debugging
    #for x in range(1, len(data)):
    #    print("x: ", data[x][1])
    #for y in range(1, len(data)):
    #    print("y: ", data[y][1])
    #for z in range(1, len(data)):
    #    print("z: ", data[z][1])

# Use this method to get any value from the data when importing this file
def getValue(x, y):
    return data[x][y]