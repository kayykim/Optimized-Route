import pandas as pd 
import folium
import openrouteservice as ors



sheet_id= '1TepU9j_QfklHsPXu9GdFnl-jkdv4_syZkE2ArU_u3Xs'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
#print(df.head())


#print(df.Latitude)
#print(df.Longitude)

coord = []
for index, row in df.iterrows():
    row_data= [row['Longitude'], row ['Latitude']]
    coord.append(row_data)
print(coord)


from scipy.spatial import distance
import itertools



# Calculate the distance matrix between all pairs of coordinates
distance_matrix = distance.cdist(coord, coord, 'euclidean')

# Initialize variables to track the best solution
min_distance = float('inf')
best_path = []

# Generate all possible permutations of the cities (excluding the starting city)
city_permutations = itertools.permutations(range(len(coord)))

# Iterate through all permutations to find the shortest path
for perm in city_permutations:
    current_distance = 0
    for i in range(len(perm) - 1):
        current_distance += distance_matrix[perm[i]][perm[i + 1]]

    # Add the distance from the last city back to the starting city
    current_distance += distance_matrix[perm[-1]][perm[0]]

    if current_distance < min_distance:
        min_distance = current_distance
        best_path = perm

# Add the distance from the last city back to the starting city for the best path
min_distance += distance_matrix[best_path[-1]][best_path[0]]

# Print the best path and minimum distance
print("Best Path:", best_path)

newlist=[]
for i in best_path:
    newlist.append(coord[i])

print(newlist)

print("Minimum Distance:", min_distance)

