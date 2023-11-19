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

    # convert all elements in list using for loops
for x in range (len(postalCode)):
    onePostalCode = postalCode[x]
    #find lat and long using open street map
    response = requests.get(f"https://nominatim.openstreetmap.org/search?format=json&postalcode={onePostalCode}")
    info = response.json()
    print (info)

    lat.append(info[0].get('lat'))
    long.append(info[0].get('long'))

    print (lat[x])
    print (long[x])
    print ('\n')
    





