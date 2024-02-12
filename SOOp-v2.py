import json
import math

class CelestialBody:
    def __init__(self, name, distance_from_sun=None, orbital_period=None, diameter=None, circumference=None):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.orbital_period = orbital_period
        self.diameter = diameter
        self.circumference = circumference
        self.moons = []
        self.planets = []

    def calculate_orbital_period(self):
        if self.distance_from_sun:
            return math.sqrt(self.distance_from_sun ** 3)

    def calculate_distance_from_sun(self):
        if self.orbital_period:
            return self.orbital_period ** (2/3)

    def calculate_moon_properties(self):
        for moon in self.moons:
            if moon.get("Diameter") and not moon.get("Circumference"):
                moon["Circumference"] = math.pi * moon["Diameter"]
            elif moon.get("Circumference") and not moon.get("Diameter"):
                moon["Diameter"] = moon["Circumference"] / math.pi

    def calculate_planet_properties(self):
        if self.diameter and not self.circumference:
            self.circumference = math.pi * self.diameter
        elif self.circumference and not self.diameter:
            self.diameter = self.circumference / math.pi

        self.calculate_moon_properties()

def calculate_total_planets_volume(planets):
    total_volume = 0
    for planet in planets:
        if planet.diameter:
            total_volume += (4/3) * math.pi * (planet.diameter / 2) ** 3
    return total_volume

# JSON data hardcoded
solar_system_data = """
{
  "Name": "Sol",
  "Diameter": 1400000,
  "Planets": [
    {
      "Name": "Mecury",
      "OrbitalPeriod": 0.39,
      "Circumference": 15329
    },
    {
      "Name": "Venus",
      "DistanceFromSun": 0.72,
      "Diameter": 12104
    },
    {
      "Name": "Earth",
      "DistanceFromSun": 1,
      "OrbitalPeriod": 1,
      "Diameter": 12756,
      "Circumference": 40075,
      "Moons": [
        {
          "Name": "Luna",
          "Diameter": 3474,
          "Circumference": 10917
        }
      ]
    },
    {
      "Name": "Mars",
      "DistanceFromSun": 1.52,
      "Circumference": 21344,
      "Moons": [
        {
          "Name": "Phobos",
          "Diameter": 22.5
        },
        {
          "Name": "Deimos",
          "Circumference": 39
        }
      ]
    },
    {
      "Name": "Jupiter",
      "DistanceFromSun": 5.2,
      "Diameter": 142984,
      "Moons": [
        {
          "Name": "Ganymede",
          "Diameter": 5268
        },
        {
          "Name": "Callisto",
          "Circumference": 4820.6
        },
        {
          "Name": "Io",
          "Circumference": 3643.2
        }
      ]
    },
    {
      "Name": "Saturn",
      "DistanceFromSun": 9.54,
      "Diameter": 120536,
      "Moons": []
    },
    {
      "Name": "Uranus",
      "DistanceFromSun": 19.2,
      "Diameter": 51118
    },
    {
      "Name": "Neptune",
      "DistanceFromSun": 30.06,
      "Diameter": 49528
    }
  ]
}
"""

solar_system = json.loads(solar_system_data)

# Create sun object
sun = CelestialBody(solar_system["Name"], diameter=solar_system["Diameter"])

# Create planet objects
for planet_data in solar_system["Planets"]:
    planet = CelestialBody(planet_data["Name"],
                           distance_from_sun=planet_data.get("DistanceFromSun"),
                           orbital_period=planet_data.get("OrbitalPeriod"),
                           diameter=planet_data.get("Diameter"),
                           circumference=planet_data.get("Circumference"))

    # Add moons to the planet
    for moon_data in planet_data.get("Moons", []):
        moon = CelestialBody(moon_data["Name"],
                             diameter=moon_data.get("Diameter"),
                             circumference=moon_data.get("Circumference"))
        planet.moons.append(moon)

    sun.planets.append(planet)

# Calculate and retrieve information
print("Name of our sun:", sun.name)
print("Diameter of the sun given its circumference:", sun.diameter)
print("Circumference of the sun given its diameter:", sun.circumference)

for planet in sun.planets:
    print("\nPlanet:", planet.name)
    print("Distance from the sun:", planet.distance_from_sun)
    print("Orbital period:", planet.orbital_period)
    print("Planet's diameter given its circumference:", planet.diameter)
    print("Planet's circumference given its diameter:", planet.circumference)

    for moon in planet.moons:
        print("\nMoon:", moon.name)
        print("Moon's diameter given its circumference:", moon.diameter)
        print("Moon's circumference given its diameter:", moon.circumference)

# Compare volumes of sun 
total_planets_volume = calculate_total_planets_volume(sun.planets)
sun_volume = (4/3) * math.pi * (sun.diameter / 2) ** 3

if total_planets_volume > sun_volume:
    print("\nThe sum of the planets' volumes is greater than the volume of the Sun.")
else:
    print("\nThe sum of the planets' volumes is not greater than the volume of the Sun.")
