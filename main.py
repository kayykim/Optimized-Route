import requests
import geopy
import folium
from pprint import pprint

#have user input as many stops
num_locations = int(input("Enter number of locations: "))

#make a list to put all the location postal addresses
addresses = []
#list to store lat and long coordinates
latitude = []
longitude = []

#have user enter in the postal code of locations
for x in range (num_locations):
    #have user enter location address
    new_location = input("Enter postal code: ")
    addresses.append(new_location)

#using the list, find the latitude and long of each
print ("Your entered addresses: ", addresses)

#counter variable
c = 0

while c < num_locations:
    #find post code from addresses array
    postcode = addresses[c]

    # find lat and long from postcode
    response = requests.get(f"https://nominatim.openstreetmap.org/search?format=json&postalcode={postcode}")
    data = response.json()

    # add lat coordinates to array latitude
    latitude.append(data[0].get('lat'))

    # add long coordinates to array longitude
    longitude.append(data[0].get('lon'))

    print (latitude[c])
    print (longitude[c])

    print ('\n')
    print (latitude[c], longitude[c])
    print (c)
    print ('\n')

    #increment counter (c) to print out next coord variables
    c += 1

#store location
location1 = (latitude[0], longitude[0])
print (location1)

location2 = (latitude[1], longitude[1])
print (location2)

'''

#mark the locations on map

location1 = float(latitude1), float(longitude1)
location2 = float(latitude2), float(longitude2)

m = folium.Map(location=location1, width= 800, height= 400)

folium.Marker(location1, popup="REV").add_to(m)
folium.Marker(location2, popup="CMH").add_to(m)

m.save("map.html")

#find the distance between two points
from geopy.distance import distance

km = distance (location1, location2)

#print text of m
print (m)
'''