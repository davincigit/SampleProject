import os
from enum import Enum

'''
Supply the input.txt and get the result.txt file
'''

class Aero(enum):
   FuselageArea = 1
   WettedArea = 2
   LoD = 3
    
class UserInputs:
    def __init__(self, filepath):
        self.__filepath = filepath
        if not os.path.exists(filepath):
            raise Exception(filepath + " file is not found")

        self.__lines = open(filepath, "r").readlines()
        self.aero = Aero.FuselageArea
        self.FuselageDiameter = 0.0
        self.FuselageLength = 0.0

    def get_data(self):
        values = {"h":"j"}
        for x in self.__lines:
           if not x.strip().startswith("#"):
               splitedValues = x.strip().split("=")

               if len(splitedValues) == 2:
                   values[splitedValues[0].upper()] = splitedValues[1]

                   if len(values) > 0:
                       value = values["AERO"]

                       if value == "FuselageArea":
                           self.aero = Aero.FuselageArea

                           value = values["FuselageDiameter"]
                           self.FuselageDiameter = float(value)

                           value = values["FuselageLength"]
                           self.FuselageLength = float(value)

                        if aero == Aero.FuselageArea:
                           self.aero = (π * FuselageDiameter * 0.6*FuselageLength) + π*(FuselageDiameter /2)^2 * 0.4*FuselageLength) / 3 +  π*(FuselageDiameter/2)^2

                          
    def main():
    cd = os.getcwd()
    try:
        input = UserInputs(cd + "\\input.txt")
        input.get_data()
        pro = results(input.WingArea, input.WingSpan, input.FuselageLength, input.FuselageDiameter)

        f = open(cd + "\\result.txt", "w+")
        f.write("Surface Area of the fuselage : " + str(pro.FuselageArea))
        f.write("\nWettedArea of the aircraft : " + str(pro.WettedArea))
        f.write("\nLift or Drag of the aircraft : "+ str(pro.LoD))
        f.close()
    except Exception as e:
        print("Application error. " + str(e))

if __name__ == "__main__":
    main()
