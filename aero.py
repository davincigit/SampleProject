import os
from enum import Enum

'''
Supply the input.txt and get the result.txt file
'''

class aero(enum):
    WingSpan = 1
    WingArea = 2
    FuselageLength = 3
    FuselageDiameter = 4

class UserInputs:
    def __init__(self, filepath):
        self.__filepath = filepath
        if not os.path.exists(filepath):
            raise Exception(filepath + " file is not found")

        self.__lines = open(filepath, "r").readlines()
        self.aero = aero.WingSpan
        self.aero = aero.WingArea
        self.aero = aero.FuselageLength
        self.aero = aero.FuselageDiameter

class AspectRatio:
        def __init__(self, aero:WingSpan, WingArea):
            self.AspectRatio = WingSpan^2 / WingArea
            return super().__init__(AspectRatio)

             class fuselageArea:
                def __init__(self, aero:FuselageDiameter, FuselageLength, FuselageDiamete, FuselageLength, FuselageDiameter):
                    self.FuselageArea = (π * FuselageDiameter * 0.6*FuselageLength) + π*(FuselageDiameter /2)^2 * 0.4*FuselageLength) / 3 +  π*(FuselageDiameter/2)^2
                    return super().__init__(FuselageArea)

               class WettedArea:
                   def __init__(self, FuselageArea, WingArea, FuselageDiameter, WingArea, WingSpan, FuselageDiameter, FuselageLength, FuselageDiameter, FuselageDiameter ):
                       self. WettedArea = FuselageArea + 2*WingArea - 2*FuselageDiameter*(WingArea/WingSpan) + 4*(1.25*FuselageDiameter)*(0.125*FuselageLength) + 2*(1.5*FuselageDiameter)*(0.15*FuselageDiameter)
                       return super().__init__(*args, **kwargs)

                   class liftDrag:
                       def __init__(self, AspectRatio, WettedArea, WingArea, AspectRatio):
                           self.LoD = 10.0+4*(AspectRatio/(WettedArea/WingArea)-1.0)
                           return super().__init__(LoD)

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
