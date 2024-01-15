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
    
def get_postalCodes():
    id = []
    # 1. Import spreadsheet
    data = pd.read_excel('address_list.xlsx') # data is the variable that stores the excel file
   
    # Variable postalCode contains all the lists of postal codes
    pc = data['Postal Code'].tolist()

    for i in range(len(pc)):
        id.append(i)
    return pc, id




