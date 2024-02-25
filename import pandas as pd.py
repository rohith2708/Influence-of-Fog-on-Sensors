import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
import glob

# Folder path containing the CSV files
folder_path_main = '/Users/Rohith Sai/CBuilding/'
path_clear = f"{folder_path_main}/CBuilding/csv/c_building_pedestrian_clear_anon/"
path_fog = f"{folder_path_main}/CBuilding/csv/c_building_pedestrian_fog_anon/"

def update_data(folder_path, sensor_type,weather): 
    dir = f"{folder_path}/{sensor_type}/"
# File pattern to match CSV files
    file_pattern = dir + '*.csv'

# Initialize an empty DataFrame to store the combined data
    combined_data = pd.DataFrame()

# Use glob to get a list of CSV files matching the pattern
    csv_files = glob.glob(file_pattern)
# Loop through each file and append its data to the combined_data DataFrame
    for csv_file in csv_files:
    # Read the CSV file
   # current_data = pd.read_csv(csv_file)
   
          current_data = pd.read_csv(csv_file,header=None,sep = ' ')
          my_data = current_data.iloc[:, :3].astype(float)
    # Combine the first three columns and convert to float
          combined_data = pd.concat([combined_data, my_data.iloc[:, :3].astype(float)], ignore_index=True)
    # Display the combined data
    my_data_square = np.square(combined_data)
    #print(my_data_square)
    sum_along_row = my_data_square.sum(axis=1)
    #print(sum_along_row)
    square_rt = np.sqrt(sum_along_row)
         # print(square_rt)
    square_rt.plot(kind = 'hist', bins=40, range=[0, 40])
    #plt.hist(Result, bins=40, range=[0, 40])
    plt.title("Histogram of {} sensor with {}".format(sensor_type, weather))
    plt.xlabel('Distance')
    plt.ylabel('No. of points')

    plt.show()

    return(combined_data)   

#def dist_calc
blickfeld_clear_data = update_data(path_clear, 'blickfeld', 'Fog')
blickfeld_fog_data = update_data(path_fog, 'blickfeld', 'Clear')
#print(blickfeld_clear_data)