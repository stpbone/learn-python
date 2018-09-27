# Create a dictionary with keys and values
winterbike = {
  "brand": "Trek",
  "model": "Madone",
  "year": 2014
}

summerbike = {
    "brand": "BMC",
    "color": "Black",
    "type": "Road",
    "year": 2011
}

trackbike = {
    "brand": "Dolan",
    "color": "Black",
    "type": "Track",
    "year": 2011
}

mountainbike = {
    "brand": "Specialized",
    "color": "Orange",
    "type": "Mountain",
    "year": 2012
}

# Use 'get' function to get the values of specificed keys within the dictionary
y = winterbike.get("year")

a = summerbike.get("brand")
b = summerbike.get("type")

c = trackbike.get("type")

print(y)

print(a)
print(b)
print(c)

# print values for all keys in the dictionary
for x in winterbike:
    print(x)

for x in trackbike:
    print(x)

# get all values in a specified dictionary
d = winterbike.values()
print(d)

e = mountainbike.values()
print(e)