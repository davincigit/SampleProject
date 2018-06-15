import os

class InputFileReading:
    def __init__(self, filepath):
        self.__filepath = filepath
        if not os.path.exists(filepath):
            raise Exception(filepath + "File is not found")
        
        self.__line = open(filepath, "r").readlines()
        self.WingArea = 0.0
        self.WingSpan = 0.0
        self.FuselageLength = 0.0
        self.FuselageDiameter = 0.0

    def get_value(self):
        values = {"h":"j"}
        for x in self.__lines:
            splitedValues = x.strip().split("=")

            if len(splitedValues) == 2:
                values[splitedValues[0].upper()] = splitedValues[1]

        if len(values) > 0:
            value = values["WINGAREA"]
            self.WingArea = float(value)

            value = values["WINGSPAN"]
            self.WingSpan = float(value)

            value = values["FUSELAGELENTH"]
            self.FuselageLength = float(value)

            value = values["FUSELAGEDIAMETER"]
            self.FuselageDiameter = float(value)

class Calculate:
    def __init__(self, WingArea, WingSpan, FuselageLength, FuselageDiameter):
        self.AspectRatio = 0.0
        self.FuselageArea = 0.0
        self.WettedArea = 0.0
        self.LoD = 0.0

        self.AspectRatio = WingSpan ** 2 / WingArea

        self.FuselageArea = (3.14159 * (FuselageDiameter * 0.6 * FuselageLength) + 3.14159 * ((FuselageDiameter / 2) ** 2) * 0.4 * FuselageLength) / 3 + 3.14159 * ((FuselageDiameter / 2) ** 2)
        self.WettedArea = FuselageArea + 2 * WingArea - 2 * FuselageDiameter *(WingArea/WingSpan) + 4 * (1.25 * FuselageDiameter) * (0.125 * FuselageLength) + 2 * (1.5 * FuselageDiameter) * (0.15 * FuselageDiameter)
        self.LoD = 10.0 + 4 * ( AspectRatio / (WettedArea/WingArea) - 1.0)

def main():
    cd = os.getcwd()
    try:
        input = InputFileReading(cd + "\\input.txt")
        input.get_value()

        cal = Calculate(input.WingArea, input.WingSpan, input.FuselageLength, input.FuselageDiameter)

        f = open(cd + "\\result.txt", "w+")
        f.write("FUSELAGEAREA :"+str(cal.FuselageArea))
        f.write("WETTEDAREA :"+str(cal.WettedArea))
        f.write("LoD :"+ str(cal.LoD))
    except Exception as e:
        print("Application Error."+str(e))

if __name__ == "__main__":
    main()


        
     
