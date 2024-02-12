import json
import math
class sun_c:
    def __init__(self, Name,circumference = None, diameter = None):
        self.name = Name
        self.planets = []
        if circumference == None: self.circumference = math.pi * diameter

        else: self.circumference = circumference

        if diameter == None: self.diameter = circumference / math.pi
        else: 
            self.diameter = diameter

#loading json data
sun_d = json.loads(ssJson)

if "Diameter" in sun_d:
    sun_o = sun_c(sun_c["Name"], diameter = sun_d["Diameter"])
if "circumference" in sun_d:
    sun_o = sun_c (sun_d["Name"], circumference = sun_d ["circumference"])

print(sun_o.name)
print(sun_o.circumference)
print(sun_o.diameter)
        