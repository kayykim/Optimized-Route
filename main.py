# Goal of code: 
# 1. Import Excel Spreadsheet
# 2. Convert postal code into latitude and longitude
# 3. Make them available in global variables

import pandas as pd # for working with data sets
import openpyxl # for getting info from excel
import folium # for visualizing data
import geopy # for locating coods from addresses

# Libraries we might not need if we use google API
import requests # for making HTTP requests
#line 35 -- using open street map (could use google maps?)



# 1. Import spreadsheet
sheet_id = '1TepU9j_QfklHsPXu9GdFnl-jkdv4_syZkE2ArU_u3Xs' # Must be changed with specific execl address
data = pd.read_excel('address_list.xlsx') # data is the variable that stores the excel file

    # Variable postalCode contains all the lists of postal codes
postalCode = data['Postal Code'].tolist()


# 2. Convert Postal Codes into lat and long

    # initalize list 
lat = []
long = []
coords = []

    # convert all elements in list using for loops
for x in range (len(postalCode)):
    onePostalCode = postalCode[x]
    #find lat and long using open street map
    response = requests.get(f"https://nominatim.openstreetmap.org/search?format=json&postalcode={onePostalCode}")
    info = response.json()

    lat.append(info[0].get('lat'))
    long.append(info[0].get('long'))

    # put these into coordinates 
    # represented as (long, lat, long, lat)
counter = 0 # make sure the correct 
alt_counter = 0 # alternates betwee long and lat

while counter < len(lat):
    if alt_counter == 0:
        coords.append(long[counter])
        alt_counter = 1

    else:
        coords.append(lat[counter])
        alt_counter = 0
        counter += 1

    print (coords)
    print ('\n')
    





