#       plateNumber, lat, lng
data = [["AZS413", 17.546, 14.156],
        ["AZS414", 18.741, 14.464],
        ["LCY476", 10.451, 16.464],
        ["LCY480", 14.454, 14.454],
        ["LNY471", 18.464, 14.164],
        ["WNA475741", 14.864, 14.494],
        ["LCY480", 14.454, 14.454],
        ["LCY480", 14.454, 14.454],
        ["WNA475741", 14.864, 14.494],
        ["LCY480", 14.455, 14.454],
        ["AZS414", 18.741, 14.464],
        ["LCY476", 10.451, 16.467]]

carsLastPosition = dict()
carsMovementCount = dict() # ...
for elements in data:
    plateNumber = elements[0]
    lat = elements[1]
    lng = elements[2]

    if plateNumber in carsLastPosition:
        print(plateNumber + " already exists in carsPositions.")

    carsLastPosition[plateNumber] = [lat, lng]