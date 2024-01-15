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

# initalization
index = []
postalCode = []
lat_coords = []
long_coords = []
distance_list = []
path = []

def main():
    sheet_id = '1TepU9j_QfklHsPXu9GdFnl-jkdv4_syZkE2ArU_u3Xs' # Must be changed with specific execl address
    postalCode, index = get_postalCodes() # get a list of postal codes
    lat_coords, long_coords, distance_list = get_coords(postalCode)
    distance_list = get_distance(distance_list)
    
def get_postalCodes():
    id = []
    # 1. Import spreadsheet
    data = pd.read_excel('address_list.xlsx') # data is the variable that stores the excel file
   
    # Variable postalCode contains all the lists of postal codes
    pc = data['Postal Code'].tolist()

    for i in range(len(pc)):
        id.append(i)
    return pc, id

def get_coords(pc):
    lat = []
    long = []
    d_array = []

    # 2. Convert Postal Codes into lat and long

    # convert all elements in list using for loops
    for x in range (len(pc)):
        onePostalCode = pc[x]
        #find lat and long using open street map
        response = requests.get(f"https://nominatim.openstreetmap.org/search?format=json&postalcode={onePostalCode}")
        info = response.json()
        lat.append(float (info[0].get('lat')))
        long.append(float (info[0].get('lon')))
        distance = math.sqrt(lat[x]**2 + long[x]**2)
        d_array.append(distance)

    return lat, long, d_array

def get_distance(d_array):
    # Perform bubble sort to orginize the list from longest -> shortest distance
    for i in range (len(d_array) - 2):
        for j in range (len(d_array) - i - 2):
            if d_array[j+1] < d_array[j+2]:
                d_array[j+1], d_array[j+2] = d_array[j+2], d_array[j+1]
            i += 1
            j += 1

    return d_array

