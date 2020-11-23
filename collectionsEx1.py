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
for carData in data:
    plateNumber = carData[0]
    lat = carData[1]
    lng = carData[2]

    if plateNumber in carsLastPosition:
        coordinatesPair = carsLastPosition[plateNumber]
        lastLat = coordinatesPair[0]
        lastLng = coordinatesPair[1]

        if lat != lastLat or lng != lastLng:
            print("Car with plate number " + plateNumber + " has moved.")

        carsLastPosition[plateNumber] = [lastLat, lastLng]
    else:
        carsLastPosition[plateNumber] = [lat, lng]
