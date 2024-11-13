import csv

#f = open("nasaadc-main/data.csv", "r")

with open("nasaadc-main/data.csv", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
for x in range(1, 10):
    print(data[x][1])
    # for y in range(1, 10):
    #     print(data[y][1])
    #     for z in range(1, 10):
    #         print(data[z][1])
# Takes data from csv and converts to array
#data = f.read().split("\n")
#print(data)

# df = open("nasaadc-main/data.txt", "w")
# df.write(str(data))
# df.close()

# print(f.read().split())
