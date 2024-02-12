import json
import math

def calculate_orbital_period(distance_from_sun):
    if distance_from_sun:
        return math.sqrt(distance_from_sun ** 3)

def calculate_distance_from_sun(orbital_period):
    if orbital_period:
        return orbital_period ** (2/3)

def calculate_moon_properties(moons):
    for moon in moons:
        if moon.get("Diameter") and not moon.get("Circumference"):
            moon["Circumference"] = math.pi * moon["Diameter"]
        elif moon.get("Circumference") and not moon.get("Diameter"):
            moon["Diameter"] = moon["Circumference"] / math.pi

def calculate_planet_properties(diameter, circumference, moons):
    if diameter and not circumference:
        circumference = math.pi * diameter
    elif circumference and not diameter:
        diameter = circumference / math.pi

    calculate_moon_properties(moons)

def calculate_total_planets_volume(planets):
    total_volume = 0
    for planet in planets:
        if planet.get("Diameter"):
            total_volume += (4/3) * math.pi * (planet["Diameter"] / 2) ** 3
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
sun = {
    "Name": solar_system["Name"],
    "Diameter": solar_system["Diameter"],
    "Planets": []
}

# Create planet objects
for planet_data in solar_system["Planets"]:
    planet = {
        "Name": planet_data["Name"],
        "DistanceFromSun": planet_data.get("DistanceFromSun"),
        "OrbitalPeriod": planet_data.get("OrbitalPeriod"),
        "Diameter": planet_data.get("Diameter"),
        "Circumference": planet_data.get("Circumference"),
        "Moons": []
    }

    # Add moons to the planet
    for moon_data in planet_data.get("Moons", []):
        moon = {
            "Name": moon_data["Name"],
            "Diameter": moon_data.get("Diameter"),
            "Circumference": moon_data.get("Circumference")
        }
        planet["Moons"].append(moon)

    sun["Planets"].append(planet)

# Calculate and retrieve information
print("Name of our sun:", sun["Name"])
print("Diameter of the sun given its circumference:", sun["Diameter"])
print("Circumference of the sun given its diameter:", sun["Diameter"] * math.pi)

for planet in sun["Planets"]:
    print("\nPlanet:", planet["Name"])
    print("Distance from the sun:", planet["DistanceFromSun"])
    print("Orbital period:", planet["OrbitalPeriod"])
    print("Planet's diameter given its circumference:", planet["Diameter"])
    print("Planet's circumference given its diameter:", planet["Circumference"])

    for moon in planet["Moons"]:
        print("\nMoon:", moon["Name"])
        print("Moon's diameter given its circumference:", moon["Diameter"])
        print("Moon's circumference given its diameter:", moon["Circumference"])

# Check if the sum of the planets' volumes is greater than the volume of the Sun
total_planets_volume = calculate_total_planets_volume(sun["Planets"])
sun_volume = (4/3) * math.pi * (sun["Diameter"] / 2) ** 3

if total_planets_volume > sun_volume:
    print("\nThe sum of the planets' volumes is greater than the volume of the Sun.")
else:
    print("\nThe sum of the planets' volumes is not greater than the volume of the Sun.")
