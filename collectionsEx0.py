def getConstantNumber():
    return 5

carAttributes = dict()
carAttributes["LCY480"]["transmission"] = "automatic"
carAttributes["LCY480"]["power"] = 97
carAttributes["LCY480"]["currentPosition"] = [12.78, 44.71]
carAttributes["LCY480"][""] = 1
carAttributes["LCY480"][getConstantNumber()] = 4
carAttributes["LCY480"][87] = 12

carAttributes["LCY485"]["transmission"] = "manual"
carAttributes["LCY485"]["power"] = 152
carAttributes["LCY485"]["currentPosition"] = [59.78, 48.71]
carAttributes["LCY485"][""] = 1
carAttributes["LCY485"][getConstantNumber() - 1] = 4
carAttributes["LCY485"][87] = 12

print(carAttributes.keys())
print("\n")
print(carAttributes.values())